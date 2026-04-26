# SideWinder APT DLL Sideloading 시나리오
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
| **위협 그룹** | SideWinder (T-APT-04) |
| **시나리오 목표** | DLL Sideloading을 통한 악성코드 실행 및 지속성 확보 |
| **핵심 기법** | vsstrace.dll Sideloading, ConfuserEx 난독화, 외부 OLE 객체 주입 |
| **MITRE ATT&CK** | T1574.002 (DLL Side-Loading), T1027 (Obfuscated Files) |

---

## 공격 흐름

```
[Initial Access — T1566.001]
  스피어피싱 이메일 + 악성 문서 첨부
        ↓
[Execution — T1204.002]
  사용자가 문서 파일 실행
        ↓
  외부 OLE 객체 주입 → 원격 템플릿 로드
        ↓
[Defense Evasion — T1574.002]
  정상 실행 파일과 동일 디렉토리에 악성 DLL 배치
        ↓
  정상 프로세스가 vsstrace.dll 로드 (DLL Sideloading)
        ↓
  ConfuserEx 난독화된 페이로드 실행
        ↓
[Discovery — T1082, T1057]
  시스템 정보 / 프로세스 목록 / 네트워크 정보 수집
        ↓
[C2 — T1071.001]
  HTTP/HTTPS 기반 C2 통신
        ↓
[Collection — T1005]
  문서, 자격증명 등 데이터 수집
        ↓
[Exfiltration — T1041]
  C2 채널을 통한 데이터 유출
```

---

## 핵심 기법 분석

### DLL Sideloading (T1574.002)

정상 서명된 실행 파일이 같은 디렉토리의 DLL을 우선 로드하는 Windows DLL 검색 순서를 악용합니다.

```
정상 실행 파일 (서명됨)
    ↓ LoadLibrary("vsstrace.dll")
    ↓ DLL 검색 순서: 실행 파일 디렉토리 → System32 → PATH
    ↓
악성 vsstrace.dll (같은 디렉토리에 배치)
    ↓
악성 코드 실행 (정상 프로세스 컨텍스트)
```

**탐지 우회 효과:**
- 정상 서명된 프로세스 내에서 실행 → AV 화이트리스트 우회
- 파일 자체에 악성 시그니처 없음 (정상 DLL 이름 사용)
- ConfuserEx 난독화로 정적 분석 방해

### 외부 OLE 객체 주입

```
문서 파일 (.docx)
    ↓ 내장된 외부 OLE 객체 참조
    ↓ http://malicious-server/template.dotm 로드
    ↓
원격 매크로 템플릿 실행
    ↓
DLL + 정상 바이너리 드롭
```

### ConfuserEx 난독화 특징

| 기법 | 설명 |
|------|------|
| Control Flow | 제어 흐름 난독화 (switch 분산) |
| String Encryption | 문자열 런타임 복호화 |
| Anti-Debug | 디버거 감지 시 종료 |
| Anti-Dump | 메모리 덤프 방지 |
| Name Obfuscation | 클래스/메서드 이름 난독화 |

---

## 탐지 방안

### Sigma Rule

```yaml
title: Suspicious DLL Sideloading - vsstrace.dll
id: 7e2c5b3a-9f4d-4e8a-b1c6-3d2f8e5b9a4c
status: stable
description: |
  vsstrace.dll이 예상 경로(System32) 외부에서 로드되는 패턴을 탐지합니다.
logsource:
    product: windows
    category: image_load
detection:
    selection:
        ImageLoaded|endswith: '\vsstrace.dll'
    filter:
        ImageLoaded|startswith:
            - 'C:\Windows\System32\'
            - 'C:\Windows\SysWOW64\'
    condition: selection and not filter
falsepositives:
    - Legitimate VSS trace DLL in non-standard paths (rare)
level: high
tags:
    - attack.defense_evasion
    - attack.persistence
    - attack.t1574.002
```

### YARA Rule

```yara
rule SideWinder_DLL_Sideload {
    meta:
        description = "SideWinder APT DLL Sideloading payload"
        author = "SOMMA RedBlue"
    strings:
        $confuser = "ConfuserEx" ascii
        $ole_remote = "http" ascii wide
        $vsstrace = "vsstrace" ascii wide nocase
        $loadlib = "LoadLibrary" ascii
    condition:
        uint16(0) == 0x5A4D and
        2 of them
}
```

---

## 대응 방안

1. Sysmon EventID 7 (Image Loaded) 로깅으로 비정상 경로 DLL 로드 탐지
2. Application Whitelisting (AppLocker/WDAC) 적용
3. 외부 OLE 객체 참조 차단 (GPO: Block external content in Office)
4. 매크로 실행 제한 정책
5. ConfuserEx 난독화 탐지 규칙 (특정 IL 패턴)

---

## 참고자료

- [MITRE ATT&CK T1574.002](https://attack.mitre.org/techniques/T1574/002/)
- [SideWinder APT — Kaspersky](https://securelist.com/sidewinder-apt/)
- [DLL Sideloading 기법 분석](https://attack.mitre.org/techniques/T1574/002/)
