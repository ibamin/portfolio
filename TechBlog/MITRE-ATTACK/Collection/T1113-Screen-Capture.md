# T1113 — Screen Capture

## 개요

**TA0009 / T1113**  
공격자가 피해 시스템의 화면을 캡처해 현재 작업 내용, 자격증명 입력, 민감한 정보를 수집하는 기법.  
내장 OS 도구 또는 악성코드를 통해 주기적/이벤트 기반으로 스크린샷 촬영.

---

## 동작 방식

- PrintScreen / WinAPI(GDI, BitBlt)로 화면 캡처
- 주기적 자동 캡처 후 C2로 전송
- 특정 윈도우(브라우저, 로그인 폼)만 선택 캡처

---

## 주요 커맨드 / 실습

### PowerShell 스크린샷
```powershell
Add-Type -AssemblyName System.Windows.Forms
$bmp = New-Object System.Drawing.Bitmap(
    [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Width,
    [System.Windows.Forms.Screen]::PrimaryScreen.Bounds.Height)
$graphics = [System.Drawing.Graphics]::FromImage($bmp)
$graphics.CopyFromScreen(0, 0, 0, 0, $bmp.Size)
$bmp.Save("C:\temp\screenshot.png")
```

### 주기적 자동 캡처 (루프)
```powershell
while ($true) {
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $path = "C:\temp\screens\$timestamp.png"
    # 위 캡처 코드 실행
    Start-Sleep -Seconds 30
}
```

### Metasploit 스크린샷
```bash
meterpreter > screenshot
meterpreter > run post/multi/gather/screen_spy
```

### Nircmd (LOLBin 활용)
```shell
nircmd.exe savescreenshotfull "C:\temp\screenshot.png"
```

---

## 탐지 방법

### 주요 이벤트
- 비정상 프로세스에서 GDI32/User32 기반 화면 캡처 API 호출
- 스크린샷 파일(.png, .bmp, .jpg) 대량 생성 (Sysmon EventID 11)
- 네트워크: 이미지 파일 외부 업로드

### Sigma Rule
```yaml
title: Suspicious Screenshot Activity
status: experimental
logsource:
  product: windows
  category: file_event
detection:
  selection:
    TargetFilename|contains: \temp\screen
    TargetFilename|endswith:
      - .png
      - .jpg
      - .bmp
  timeframe: 1m
  condition: selection | count() > 5
level: medium
tags:
  - attack.collection
  - attack.t1113
```

---

## 대응 방안

1. EDR — 비정상 화면 캡처 API 호출 탐지
2. DLP — 이미지 파일 외부 전송 모니터링
3. 화면 캡처 API 접근 감사

---

## 참고자료
- [MITRE ATT&CK T1113](https://attack.mitre.org/techniques/T1113/)
- [Metasploit Screen Spy](https://www.metasploit.com)
