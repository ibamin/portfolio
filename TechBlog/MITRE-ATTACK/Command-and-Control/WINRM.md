# WINRM

## 개요

WinRM은 Windows Remote Management의 약자로, Microsoft의 WS-Management 프로토콜 구현체입니다. PowerShell Remoting의 기반이며 HTTP/HTTPS를 통해 원격 시스템 관리를 가능하게 합니다.

## 프로세스

```mermaid
flowchart TD
    subgraph Client[클라이언트]
        A[PowerShell] --> B[WinRM Client]
        B --> C[WS-Management]
        C --> D[HTTP/HTTPS]
    end

    subgraph Target[대상 시스템]
        E[WinRM Service] --> F[WinRS]
        E --> G[PowerShell Remoting]
        E --> H[WSMan Provider]
        I[WMI Provider] --> H
    end

    D --> E
```

```mermaid
sequenceDiagram
    participant C as Client
    participant W as WinRM Service
    participant P as PowerShell Engine
    participant S as System

    C->>W: 1. WinRM 연결 요청 (5985/5986)
    W->>W: 2. 인증 검증
    W->>P: 3. PowerShell 세션 생성
    P->>S: 4. 명령어 실행
    S-->>P: 5. 실행 결과
    P-->>W: 6. 결과 직렬화
    W-->>C: 7. XML로 응답
```

## 주요 포트와 인증

- HTTP: TCP/5985
- HTTPS: TCP/5986
- 인증: Kerberos, NTLM, Basic(HTTPS), CredSSP, Certificate-based

## 명령 예시

```powershell
Enter-PSSession -ComputerName target-pc
Invoke-Command -ComputerName target-pc -ScriptBlock { Get-Process }
winrs -r:target-pc "ipconfig"
```

## 탐지 포인트

- `Microsoft-Windows-WinRM/Operational` 연결 이벤트
- PowerShell 이벤트 `4103`, `4104`
- `wsmprovhost.exe` 생성과 비정상 자식 프로세스
- 관리 구간 외부에서 발생하는 TCP/5985, 5986 연결

## 대응 방안

1. HTTPS 사용을 강제하고 Basic/CredSSP 인증을 제한합니다.
2. TrustedHosts 설정을 최소화합니다.
3. PowerShell Script Block Logging과 WinRM Operational 로그를 활성화합니다.
4. JEA(Just Enough Administration)를 적용해 원격 세션 권한을 제한합니다.

## 참고자료

- [Windows Remote Management](https://learn.microsoft.com/en-us/windows/win32/winrm/portal)
- [PowerShell Remoting Security Considerations](https://learn.microsoft.com/en-us/powershell/scripting/learn/remoting/winrmsecurity)
