# T1057 — Process Discovery

## 개요

**TA0007 / T1057**  
현재 실행 중인 프로세스 목록을 수집해 보안 솔루션, 인터레스팅 애플리케이션, AV/EDR 제품을 파악하는 기법.  
우회 전략 수립 및 타겟 프로세스 선별에 활용.

---

## 주요 커맨드 / 실습

### Windows 프로세스 열거
```shell
tasklist
tasklist /v
tasklist /svc
wmic process get name,processid,commandline,executablepath
```

```powershell
Get-Process | Select Name, Id, Path, CPU, WorkingSet
Get-Process | Where-Object {$_.Path -like "*\Windows\*"} | Select Name, Id, Path
Get-CimInstance Win32_Process | Select Name, ProcessId, CommandLine, ExecutablePath
```

### 보안 솔루션 탐지
```powershell
# AV/EDR 제품명 탐지
Get-Process | Where-Object {
    $_.Name -match "defender|mcafee|symantec|crowdstrike|carbon|cylance|sentinel|falcon|cb|edr"
}

# 보안 센터 정보
Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntiVirusProduct
```

### Linux 프로세스 열거
```bash
ps aux
ps -ef
ls -la /proc/*/exe 2>/dev/null
cat /proc/*/cmdline 2>/dev/null | tr '\0' ' '
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: Suspicious Process Discovery Commands
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    Image|endswith:
      - \tasklist.exe
      - \wmic.exe
    CommandLine|contains: 'process'
  condition: selection
level: low
tags:
  - attack.discovery
  - attack.t1057
```

---

## 대응 방안

1. EDR 프로세스 숨김 기능 활성화
2. tasklist, wmic process 실행 패턴 모니터링

---

## 참고자료
- [MITRE ATT&CK T1057](https://attack.mitre.org/techniques/T1057/)
