# T1082 — System Information Discovery

## 개요

**TA0007 / T1082**  
공격자가 침해한 시스템의 OS 버전, 하드웨어 정보, 설치된 패치, 보안 소프트웨어 등 기본 시스템 정보를 수집하는 기법입니다. 수집된 정보는 후속 공격(권한 상승, 취약점 익스플로잇) 계획 수립에 활용됩니다.

---

## 동작 방식

1. 초기 접근 후 현재 시스템 환경 파악
2. OS 버전, 아키텍처, 설치된 패치(KBs) 확인
3. 실행 중인 보안 소프트웨어(AV, EDR) 탐지
4. 수집된 정보로 취약점 분석 및 후속 공격 벡터 결정

---

## 주요 커맨드 / 실습

### Windows - 기본 시스템 정보
```cmd
# 전체 시스템 정보 수집
systeminfo

# WMI를 통한 OS 정보
wmic os get Caption,Version,BuildNumber,OSArchitecture /format:list

# 설치된 핫픽스(패치) 목록
wmic qfe list full
wmic qfe get HotFixID,InstalledOn

# 호스트명 및 네트워크 정보
hostname
ipconfig /all
```

### Windows - PowerShell 고급 수집
```powershell
# 상세 컴퓨터 정보
Get-ComputerInfo | Select-Object CsName, OsName, OsVersion, OsBuildNumber, OsArchitecture

# 설치된 패치 목록
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object HotFixID, InstalledOn, Description

# 설치된 안티바이러스 제품 확인
Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntiVirusProduct |
    Select-Object displayName, productState, pathToSignedProductExe

# 실행 중인 서비스 목록
Get-Service | Where-Object {$_.Status -eq "Running"} | Select-Object Name, DisplayName
```

### Linux - 시스템 정보 수집
```bash
# OS 및 커널 정보
uname -a
cat /etc/os-release
cat /proc/version

# CPU 및 메모리 정보
lscpu
free -h
cat /proc/meminfo

# 네트워크 인터페이스
ip a
ip route
cat /etc/resolv.conf

# 설치된 패키지 목록 (취약한 버전 확인)
dpkg -l 2>/dev/null | head -50          # Debian/Ubuntu
rpm -qa 2>/dev/null | head -50           # RHEL/CentOS
```

### WES-NG - 패치 누락 취약점 분석
```bash
# Windows 시스템에서 systeminfo 수집 후 분석
systeminfo > systeminfo.txt

# 공격자 시스템에서 WES-NG 실행
python3 wes.py systeminfo.txt
python3 wes.py systeminfo.txt -i 'Elevation of Privilege' --exploits-only
python3 wes.py systeminfo.txt -o missing_patches.csv
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: Suspicious System Information Discovery
id: d2e7a4c1-9b5f-4a3e-8c6d-2f1b9e4a7c3d
status: stable
description: Detects rapid execution of multiple system discovery commands
logsource:
    product: windows
    category: process_creation
detection:
    selection:
        Image|endswith:
            - '\systeminfo.exe'
            - '\wmic.exe'
            - '\hostname.exe'
            - '\ipconfig.exe'
    condition: selection | count() > 3
timeframe: 1m
falsepositives:
    - IT asset management tools
    - Legitimate administrative scripts
    - Software installations
level: medium
tags:
    - attack.discovery
    - attack.t1082
```

---

## 대응 방안

1. 커맨드라인 로깅 활성화 (프로세스 생성 감사 정책)
2. Sysmon 배포로 상세 프로세스 실행 이력 수집
3. EDR 솔루션을 통한 정찰 행위 패턴 탐지
4. 주요 시스템 정보 수집 도구 실행 시 알림 설정
5. 최소 권한 원칙으로 일반 사용자의 WMI 쿼리 제한

---

## 참고자료
- [MITRE ATT&CK T1082](https://attack.mitre.org/techniques/T1082/)
- [WES-NG GitHub](https://github.com/bitsadmin/wesng)
- [Sysmon Configuration](https://github.com/SwiftOnSecurity/sysmon-config)
