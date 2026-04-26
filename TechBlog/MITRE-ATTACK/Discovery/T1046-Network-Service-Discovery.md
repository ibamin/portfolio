# T1046 — Network Service Discovery

## 개요

**TA0007 / T1046**  
내부 네트워크의 활성 호스트와 열려 있는 서비스/포트를 스캔하는 기법입니다. 공격자는 스캔 결과를 바탕으로 취약한 서비스를 식별하고 후속 공격 대상을 선정합니다.

---

## 동작 방식

1. 핑 스위프로 활성 호스트 식별
2. 포트 스캔으로 열린 포트 및 실행 중인 서비스 파악
3. 서비스 버전 정보 수집 (취약점 매핑)
4. 발견된 취약 서비스를 대상으로 익스플로잇 시도

---

## 주요 커맨드 / 실습

### Nmap 종합 스캔
```bash
# 기본 버전 및 스크립트 스캔
nmap -sV -sC -oA scan_results 192.168.1.0/24

# 전체 포트 스캔
nmap -p- -T4 192.168.1.10

# OS 탐지 포함 종합 스캔
nmap -A -T4 192.168.1.10

# 특정 포트 범위 스캔
nmap -p 22,80,443,3389,445,3306 192.168.1.0/24

# UDP 스캔 (SNMP, DNS 등)
nmap -sU -p 53,161,162 192.168.1.0/24

# NSE 스크립트를 이용한 취약점 스캔
nmap --script vuln 192.168.1.10
```

### Masscan - 고속 포트 스캔
```bash
# 전체 포트 초고속 스캔
masscan -p1-65535 192.168.1.0/24 --rate=10000

# 특정 포트 스캔
masscan -p80,443,8080,8443 192.168.0.0/16 --rate=5000

# 결과 저장
masscan -p1-65535 192.168.1.0/24 --rate=1000 -oX scan_results.xml
```

### Netstat - 로컬 서비스 확인
```cmd
# 현재 시스템에서 열려 있는 포트 및 연결 확인
netstat -ano

# 특정 포트 필터링
netstat -ano | findstr ":3389"
netstat -ano | findstr "LISTENING"

# Linux
netstat -tlnp
ss -tlnp
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: Network Port Scanner Execution
id: f3b8a5e2-7c4d-4e1b-9a6f-2d8c5e7b3a1f
status: stable
description: Detects execution of common network scanning tools
logsource:
    product: windows
    category: process_creation
detection:
    selection:
        Image|endswith:
            - '\nmap.exe'
            - '\masscan.exe'
            - '\zmap.exe'
    condition: selection
falsepositives:
    - Authorized penetration testing
    - Network administrators performing inventory
level: high
tags:
    - attack.discovery
    - attack.t1046
```

---

## 대응 방안

1. 네트워크 세그멘테이션으로 불필요한 서비스 접근 제한
2. IDS/IPS 규칙으로 포트 스캔 패턴 탐지
3. 방화벽에서 불필요한 포트 차단
4. 네트워크 플로우 분석으로 비정상 스캔 트래픽 탐지
5. 허니팟 서비스 운영으로 스캔 행위 조기 탐지

---

## 참고자료
- [MITRE ATT&CK T1046](https://attack.mitre.org/techniques/T1046/)
- [Nmap 공식 문서](https://nmap.org/docs.html)
- [Masscan GitHub](https://github.com/robertdavidgraham/masscan)
