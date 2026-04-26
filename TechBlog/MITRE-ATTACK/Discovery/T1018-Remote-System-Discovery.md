# T1018 — Remote System Discovery

## 개요

**TA0007 / T1018**  
내부 네트워크에서 다른 시스템을 식별하는 기법입니다. 공격자는 ARP 캐시, DNS 쿼리, NetBIOS, LDAP 등을 활용하여 접근 가능한 시스템 목록을 파악하고 횡이동(Lateral Movement)의 대상을 발굴합니다.

---

## 동작 방식

1. 현재 시스템의 네트워크 연결 정보 및 ARP 캐시 확인
2. NetBIOS, DNS, LDAP 쿼리로 도메인 내 시스템 열거
3. 핑 스위프, 포트 스캔으로 활성 호스트 확인
4. 발견된 시스템 중 취약하거나 권한이 있는 대상 선정

---

## 주요 커맨드 / 실습

### ARP 캐시 및 네트워크 기본 탐색
```cmd
# ARP 캐시 확인 (이미 통신한 호스트 목록)
arp -a

# 공유 리소스 열거
net view
net view /domain

# 현재 세션 확인
net session
net use

# DNS를 통한 도메인 컨트롤러 확인
nslookup -type=SRV _ldap._tcp.dc._msdcs.corp.local
nslookup -type=SRV _kerberos._tcp.corp.local
```

### Active Directory - PowerShell
```powershell
# AD에서 컴퓨터 계정 열거
Get-ADComputer -Filter * -Properties * | Select-Object Name, OperatingSystem, IPv4Address

# 특정 OS 필터링
Get-ADComputer -Filter {OperatingSystem -like "*Server*"} | Select-Object Name, OperatingSystem

# 도메인 컨트롤러 목록
Get-ADDomainController -Filter * | Select-Object Name, IPv4Address, IsGlobalCatalog
```

### PowerShell 핑 스위프
```powershell
# 서브넷 전체 핑 스위프
1..254 | ForEach-Object {
    $ip = "192.168.1.$_"
    if (Test-Connection -ComputerName $ip -Count 1 -Quiet -ErrorAction SilentlyContinue) {
        Write-Host "[+] $ip is alive"
    }
}

# 병렬 핑 스위프 (빠른 버전)
1..254 | ForEach-Object -Parallel {
    $ip = "192.168.1.$_"
    if (Test-Connection -ComputerName $ip -Count 1 -Quiet -ErrorAction SilentlyContinue) {
        "$ip"
    }
} -ThrottleLimit 50
```

### PowerView
```powershell
Import-Module .\PowerView.ps1

# 도메인 내 모든 컴퓨터 열거
Get-NetComputer
Get-NetComputer -OperatingSystem "*Server*"

# 로컬 관리자 권한이 있는 시스템 찾기
Find-LocalAdminAccess

# 현재 사용자가 관리자인 시스템 찾기
Find-LocalAdminAccess -Verbose
```

### CrackMapExec
```bash
# 서브넷에서 SMB 서명 비활성화 호스트 목록 (NTLM 릴레이 대상)
crackmapexec smb 192.168.1.0/24 --gen-relay-list relay_targets.txt

# 유효 자격증명으로 접근 가능한 시스템 확인
crackmapexec smb 192.168.1.0/24 -u administrator -p 'Password123!'
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: Remote System Discovery via Net Commands
id: c1a8e5f2-3d7b-4e9c-a6f1-8b2d5e7a4c3f
status: stable
description: Detects use of net.exe for remote system and session discovery
logsource:
    product: windows
    category: process_creation
detection:
    selection:
        Image|endswith: '\net.exe'
        CommandLine|contains:
            - ' view'
            - ' session'
    condition: selection
falsepositives:
    - IT administrators performing legitimate network inventory
    - Monitoring tools
level: low
tags:
    - attack.discovery
    - attack.t1018
```

---

## 대응 방안

1. 네트워크 세그멘테이션으로 불필요한 내부 통신 차단
2. LDAP 쿼리 모니터링 (과도한 AD 열거 탐지)
3. ARP 스캔 탐지 IDS 규칙 적용
4. NetBIOS/LLMNR 비활성화
5. 도메인 컴퓨터 열거 감사 로그 활성화

---

## 참고자료
- [MITRE ATT&CK T1018](https://attack.mitre.org/techniques/T1018/)
- [PowerView GitHub](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1)
- [CrackMapExec GitHub](https://github.com/byt3bl33d3r/CrackMapExec)
