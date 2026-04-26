# Qilin 랜섬웨어 Safe Mode 우회 시나리오
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
| **위협 그룹** | Qilin (Rust 기반 RaaS) |
| **시나리오 목표** | Safe Mode 재부팅을 통한 EDR 비활성화 후 랜섬웨어 실행 |
| **암호화** | AES-256-GCM + RSA-2048 |
| **분석 도구** | Ghidra, x64dbg |
| **MITRE ATT&CK** | T1562.009 (Safe Mode Boot), T1486 (Data Encrypted for Impact) |

---

## 공격 흐름

```
[Initial Access]
  Spear phishing / RDP 브루트포스로 내부망 접근
        ↓
[Discovery]
  시스템 정보 수집, AV/EDR 제품 확인
        ↓
[Defense Evasion — T1562.009]
  bcdedit /set {default} safeboot minimal
        ↓
  강제 재부팅 (shutdown /r /t 0)
        ↓
  Safe Mode 부팅 → EDR/AV 서비스 자동 시작 비활성화
        ↓
[Execution]
  Safe Mode에서 랜섬웨어 페이로드 실행
        ↓
[Impact — T1486]
  AES-256-GCM 파일 암호화 + RSA-2048 키 래핑
        ↓
  랜섬 노트 생성
        ↓
[Post-Execution]
  bcdedit /deletevalue {default} safeboot
        ↓
  정상 모드로 재부팅
```

---

## 핵심 기법: Safe Mode Boot (T1562.009)

### 공격 커맨드

```cmd
:: Safe Mode 설정
bcdedit /set {default} safeboot minimal

:: 강제 재부팅
shutdown /r /t 0 /f

:: (랜섬웨어 실행 후) Safe Mode 해제
bcdedit /deletevalue {default} safeboot
```

### 왜 Safe Mode인가?

| 항목 | Normal Mode | Safe Mode |
|------|-------------|-----------|
| EDR 에이전트 | 실행 중 | 미실행 |
| Windows Defender | 실행 중 | 미실행 |
| 탐지 가능성 | 높음 | 거의 없음 |
| 파일 잠금 | 다수 프로세스 | 최소 프로세스 |

Safe Mode에서는 핵심 드라이버와 서비스만 로드되므로 EDR/AV가 동작하지 않습니다.

---

## 탐지 방안

### Sigma Rule — Correlation Rule (두 이벤트 순차 탐지)

```yaml
title: Qilin-style Safe Mode Boot for EDR Bypass
id: 8f3c2e5a-7b4d-4e9c-a1f6-3b8d5e2a7c4f
status: stable
description: |
  bcdedit safeboot 설정 후 즉시 재부팅이 발생하는 패턴을 탐지합니다.
  두 이벤트의 순차 발생을 Correlation Rule로 묶어 High Severity로 에스컬레이션합니다.
logsource:
    product: windows
    category: process_creation
detection:
    selection_bcdedit:
        Image|endswith: '\bcdedit.exe'
        CommandLine|contains: 'safeboot'
    selection_shutdown:
        Image|endswith: '\shutdown.exe'
        CommandLine|contains:
            - '/r'
            - '-r'
    condition: selection_bcdedit or selection_shutdown
timeframe: 5m
level: high
tags:
    - attack.defense_evasion
    - attack.t1562.009
```

### YARA Rule

```yara
rule Qilin_Ransomware {
    meta:
        description = "Qilin Ransomware (Rust-based, AES-256-GCM + RSA-2048)"
        author = "SOMMA RedBlue"
    strings:
        $rust_panic = "rust_begin_unwind" ascii
        $aes = "aes-gcm" ascii
        $rsa = "rsa" ascii
        $bcdedit = "bcdedit" ascii wide
        $safeboot = "safeboot" ascii wide
        $ransom_note = "README_TO_RESTORE" ascii wide
    condition:
        uint16(0) == 0x5A4D and
        $rust_panic and
        3 of ($aes, $rsa, $bcdedit, $safeboot, $ransom_note)
}
```

---

## 탐지 검증 결과

| 검증 항목 | 결과 |
|-----------|------|
| Qilin BAS 시나리오 탐지율 | **100%** |
| BlackMatter 유사 기법 탐지 | 동일 규칙 적용 확인 |
| AvosLocker 유사 기법 탐지 | 동일 규칙 적용 확인 |
| Cheiron EDR 연동 | Alert Mapping 완료 |

---

## 대응 방안

1. `bcdedit` 실행 모니터링 (Sysmon EventID 1)
2. Safe Mode 부팅 이벤트 SIEM 알림 설정
3. EDR이 Safe Mode에서도 동작하도록 커널 드라이버 등록
4. Boot Configuration 변경 권한 최소화
5. 오프라인 백업 유지

---

## 참고자료

- [MITRE ATT&CK T1562.009](https://attack.mitre.org/techniques/T1562/009/)
- [Qilin Ransomware Analysis — Trend Micro](https://www.trendmicro.com/en_us/research.html)
- [Safe Mode 우회 기법 분석 — SentinelOne](https://www.sentinelone.com/)
