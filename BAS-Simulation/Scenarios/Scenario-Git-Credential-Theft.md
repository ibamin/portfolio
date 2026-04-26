# Git Credential 탈취 탐지 시나리오
<p class="doc-hero">
  <img class="doc-hero-image" src="../../assets/images/pexels-server-racks-5480781.jpg" alt="Server racks in a data center" />
  <span class="doc-hero-caption">Image: Brett Sayles / Pexels</span>
</p>
## 구조 다이어그램

```mermaid
flowchart LR
    Hypothesis["시나리오 가설"] --> Emulation["공격 에뮬레이션"]
    Emulation --> Telemetry["로그 수집"]
    Telemetry --> Detection["탐지 검증"]
    Detection --> Hardening["개선/하드닝"]
```


## 개요

| 항목 | 내용 |
|------|------|
| **시나리오 목표** | Git 자격증명 평문 저장 설정을 통한 Credential Access 시뮬레이션 |
| **핵심 기법** | `git config credential.helper store` 악용 |
| **MITRE ATT&CK** | T1552.001 (Credentials In Files) |
| **탐지 전** | 기존 EDR 탐지율 **0%** |
| **탐지 후** | 커버리지 **100%**, FP 2건 제거 |

---

## 배경

`git config credential.helper store` 설정 시 Git 자격증명이 `~/.git-credentials` 파일에 **평문**으로 저장됩니다. 공격자가 이 설정을 악용하면 개발자의 GitHub/GitLab 토큰, 패스워드를 탈취할 수 있습니다.

**기존 EDR(Cheiron)에서 전혀 탐지되지 않는 것을 발견**하여 탐지 규칙을 설계하고 검증했습니다.

---

## 공격 흐름

```
[Initial Access]
  개발자 워크스테이션 접근 (피싱, 내부 횡이동 등)
        ↓
[Discovery — T1083]
  Git 설치 여부 및 기존 credential 설정 확인
  git config --list | findstr credential
        ↓
[Credential Access — T1552.001]
  git config --global credential.helper store
        ↓
  사용자의 다음 git pull/push 시 자격증명이 평문 저장
        ↓
[Collection]
  %USERPROFILE%\.git-credentials 파일 수집
  형식: https://username:token@github.com
        ↓
[Exfiltration]
  자격증명 유출 → GitHub/GitLab 리포지토리 접근
        ↓
[Impact]
  소스코드 탈취, Supply Chain 공격, 악성 코드 주입
```

---

## 시뮬레이션 커맨드

### Windows

```powershell
# 1. Git credential store 설정 (악성 행위)
git config --global credential.helper store

# 2. 자격증명 파일 확인
type %USERPROFILE%\.git-credentials

# 3. 기존 credential 설정 확인 (정찰)
git config --list | findstr credential
reg query HKCU\Software\GitForWindows /v InstallPath 2>nul
```

### Linux

```bash
# 1. Git credential store 설정
git config --global credential.helper store

# 2. 자격증명 파일 확인
cat ~/.git-credentials

# 3. 히스토리에서 흔적 확인
grep -r "credential.helper" ~/.gitconfig
```

---

## 탐지 방안

### Sigma Rule — Windows (Sysmon EventID 1)

```yaml
title: Git Credential Helper Store Configuration
id: 5e8c3f2a-7b4d-4e9c-a1f6-3b8d5e2a7c4f
status: stable
description: |
  git config credential.helper store 설정을 탐지합니다.
  자격증명이 평문으로 디스크에 저장되는 위험한 설정입니다.
logsource:
    product: windows
    category: process_creation
detection:
    selection:
        Image|endswith: '\git.exe'
        CommandLine|contains|all:
            - 'credential.helper'
            - 'store'
    condition: selection
falsepositives:
    - 개발 환경 초기 설정 시 (CI/CD 파이프라인)
level: high
tags:
    - attack.credential_access
    - attack.t1552.001
```

### Sigma Rule — Linux (auditd)

```yaml
title: Git Credential Helper Store - Linux
id: 6f9d4a3b-8c5e-4f0a-b2d7-4c3e9f6a8b5d
status: stable
description: Linux 환경에서 git credential.helper store 설정 탐지
logsource:
    product: linux
    service: auditd
detection:
    selection:
        type: EXECVE
        a0: 'git'
        a1: 'config'
    filter:
        CommandLine|contains|all:
            - 'credential.helper'
            - 'store'
    condition: selection and filter
level: high
tags:
    - attack.credential_access
    - attack.t1552.001
```

### .git-credentials 파일 접근 탐지

```yaml
title: Git Credentials File Access
id: 7a0e5b4c-9d6f-4a1b-c3e8-5d4f0a7b9c6e
status: experimental
description: .git-credentials 파일에 대한 비정상 접근 탐지
logsource:
    product: windows
    category: file_access
detection:
    selection:
        TargetFilename|endswith: '.git-credentials'
    filter:
        Image|endswith: '\git.exe'
    condition: selection and not filter
level: high
tags:
    - attack.credential_access
    - attack.t1552.001
```

---

## 탐지 검증 결과

| 항목 | Before | After |
|------|--------|-------|
| 탐지 커버리지 | 0% | **100%** |
| False Positive | N/A | 2건 발견 → 제거 |
| Cheiron EDR 연동 | 미연동 | Alert Mapping 완료 |
| SIEM Alert | 없음 | 연동 완료 |

**FP 원인 및 처리:**
- CI/CD 파이프라인의 자동 설정 (Jenkins) → 예외 처리
- VS Code Git Extension 초기화 → 예외 처리

---

## 대응 방안

1. `credential.helper store` 대신 `credential.helper manager` (Windows) 또는 `credential.helper cache` (Linux) 사용 권장
2. `.git-credentials` 파일 존재 여부 정기 점검
3. Git Hooks로 credential.helper store 설정 차단
4. GitHub Personal Access Token 만료 기간 설정
5. SSH 키 기반 인증으로 전환

---

## 참고자료

- [MITRE ATT&CK T1552.001](https://attack.mitre.org/techniques/T1552/001/)
- [Git Credential Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage)
- [GitHub Token Security](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure)
