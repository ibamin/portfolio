# T1005 — Data from Local System

## 개요

**TA0009 / T1005**  
침해한 로컬 파일 시스템에서 문서, 데이터베이스, 설정 파일, 소스코드 등 가치 있는 데이터를 수집하는 기법입니다. 수집된 데이터는 아카이브(T1560)하여 C2 채널이나 클라우드 스토리지를 통해 유출됩니다.

---

## 동작 방식

1. 가치 있는 파일 유형 및 위치 식별 (문서, DB, 소스코드, 설정 파일)
2. 키워드 검색으로 민감 데이터 포함 파일 필터링
3. 대상 파일 수집 및 임시 디렉토리에 통합
4. 아카이브 후 유출 (T1560 + T1041/T1567)

---

## 주요 커맨드 / 실습

### Windows - 파일 유형별 검색 및 수집
```cmd
# 문서 파일 검색
dir /s /b C:\Users\*.docx C:\Users\*.xlsx C:\Users\*.pdf C:\Users\*.pptx

# 패스워드 포함 파일 검색
findstr /si "password" C:\Users\*.txt C:\Users\*.xml C:\Users\*.ini C:\Users\*.config

# 설정 파일 검색
dir /s /b C:\inetpub\*.config C:\inetpub\*.xml
dir /s /b C:\*.env C:\*.ini
```

### Windows - PowerShell 고급 수집
```powershell
# 최근 수정된 문서 파일 검색
Get-ChildItem -Path C:\Users -Recurse -Include "*.docx","*.xlsx","*.pdf","*.txt" -ErrorAction SilentlyContinue |
    Where-Object {$_.LastWriteTime -gt (Get-Date).AddDays(-30)} |
    Select-Object FullName, Length, LastWriteTime |
    Sort-Object LastWriteTime -Descending

# 키워드 포함 파일 내용 검색
Get-ChildItem -Path C:\ -Recurse -Include "*.txt","*.ini","*.xml","*.config" -ErrorAction SilentlyContinue |
    Select-String -Pattern "password|secret|credential|api_key" |
    Select-Object Path, LineNumber, Line

# 파일 수집 스크립트
$sourceDir = "C:\Users"
$destDir = "C:\temp\collected"
New-Item -ItemType Directory -Path $destDir -Force

Get-ChildItem -Path $sourceDir -Recurse -Include "*.docx","*.xlsx","*.pdf" -ErrorAction SilentlyContinue |
    ForEach-Object { Copy-Item $_.FullName -Destination $destDir -Force }
```

### Linux - 파일 수집
```bash
# 민감 파일 유형 검색
find /home -name "*.txt" -o -name "*.pdf" -o -name "*.doc" 2>/dev/null
find / -name "*.conf" -o -name "*.cfg" -o -name "*.env" 2>/dev/null | head -50

# 키워드 포함 파일 검색
grep -r "password\|secret\|api_key\|token" /etc/ 2>/dev/null
grep -r "password" /var/www/ 2>/dev/null

# 파일 수집 후 아카이브
find /home -name "*.docx" -o -name "*.xlsx" 2>/dev/null | xargs tar czf /tmp/collected.tar.gz
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: Bulk File Copy from User Directories
id: e5a3c8f1-7b4d-4e2b-9f6c-2d8a5e7b3c1f
status: experimental
description: Detects bulk file copying from user directories which may indicate data collection
logsource:
    product: windows
    category: file_event
detection:
    selection:
        TargetFilename|startswith: 'C:\Users\'
        TargetFilename|endswith:
            - '.docx'
            - '.xlsx'
            - '.pdf'
            - '.pst'
    condition: selection | count() > 50
timeframe: 1m
falsepositives:
    - Backup software
    - File migration tools
    - Legitimate bulk file operations
level: medium
tags:
    - attack.collection
    - attack.t1005
```

---

## 대응 방안

1. 파일 접근 감사 로그 활성화 (민감 디렉토리)
2. DLP(Data Loss Prevention) 솔루션으로 대량 파일 복사 탐지 및 차단
3. 데이터 분류 정책으로 민감 데이터에 접근 제어 강화
4. UBA(User Behavior Analytics)로 비정상 파일 접근 패턴 탐지
5. 중요 파일 암호화 (BitLocker, EFS)
6. 네트워크 트래픽 모니터링으로 대용량 데이터 유출 탐지

---

## 참고자료
- [MITRE ATT&CK T1005](https://attack.mitre.org/techniques/T1005/)
- [Microsoft - Advanced Threat Protection](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/)
- [NIST - Data Classification](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-60v1r1.pdf)
