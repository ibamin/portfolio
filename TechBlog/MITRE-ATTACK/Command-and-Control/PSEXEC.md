# PSEXEC

## 개요

PsExec는 Sysinternals Suite의 원격 실행 도구입니다. 원격 시스템의 `ADMIN$` 공유와 서비스 제어 관리자(SCM)를 이용해 임시 서비스를 배포하고 명령을 실행할 수 있어, 침해 사고에서는 원격 실행과 횡적 이동 흔적으로 자주 관찰됩니다.

## 동작 흐름

```mermaid
sequenceDiagram
    participant C as Client
    participant TS as Target SMB
    participant TP as Target Process
    participant TSvc as Target Service Manager

    C->>TS: 1. ADMIN$ 공유 연결
    C->>TS: 2. PSEXESVC.exe 파일 복사
    C->>TSvc: 3. 서비스 생성 요청
    TSvc->>TP: 4. PSEXESVC.exe 실행
    C->>TP: 5. Named Pipe 연결
    C->>TP: 6. 명령어 전송
    TP->>C: 7. 실행 결과 반환
    C->>TSvc: 8. 서비스 중지/삭제
    C->>TS: 9. PSEXESVC.exe 파일 삭제
```

```mermaid
flowchart TD
    subgraph Client[클라이언트 시스템]
        A[PsExec.exe] --> B[SMB 클라이언트]
        A --> C[Named Pipe 클라이언트]
    end

    subgraph Target[대상 시스템]
        D[ADMIN$ 공유] --> E[PSEXESVC.exe]
        E --> F[Named Pipe 서버]
        F --> G[명령어 실행 프로세스]
        H[Service Control Manager] --> E
    end

    B --> D
    C --> F
```

## 관찰 포인트

- `ADMIN$`, `IPC$` 공유 접근
- `PSEXESVC.exe` 파일 생성 및 삭제
- System 이벤트 로그 `7045` 서비스 생성
- Security 이벤트 로그 `4688`에서 `psexesvc.exe` 하위 프로세스 생성
- Named Pipe 기반 원격 명령 입출력

## 탐지 예시

```text
Event ID: 7045
Service Name: PSEXESVC

Event ID: 4688
Creator Process Name: psexesvc.exe
```

## 대응 방안

1. 로컬 관리자 권한과 관리 공유 접근 권한을 최소화합니다.
2. 원격 서비스 생성 이벤트를 SIEM에서 상시 모니터링합니다.
3. 관리 도구 사용 서버와 일반 엔드포인트 간 SMB 흐름을 분리해 봅니다.

## 참고자료

- [PsExec - Sysinternals](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec)
- [Service Control Manager](https://learn.microsoft.com/en-us/windows/win32/services/service-control-manager)
