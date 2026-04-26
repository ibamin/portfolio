# Scheduler

## 개요

Windows Task Scheduler는 예약 작업을 관리하고 실행하는 서비스입니다. 공격자는 예약 작업을 이용해 명령 실행, 지속성 확보, 원격 실행을 시도할 수 있습니다.

## 프로세스

```mermaid
flowchart TD
    subgraph Client[클라이언트]
        A[schtasks.exe] --> B[Task Scheduler API]
        B --> C[COM/RPC Client]
    end

    subgraph Server[서버]
        D[Schedule Service] --> E[Task Engine]
        D --> F[Task COM Server]
        E --> G[Task Runner]
        G --> H[Process Creation]
    end

    subgraph Storage[저장소]
        I[Task Store]
        J[XML Files]
        K[Registry]
    end

    C --> F
    E --> I
    I --> J
    I --> K
```

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Schedule Service
    participant E as Task Engine
    participant R as Task Runner
    participant P as Process

    C->>S: 1. 작업 생성 요청
    S->>S: 2. 권한 검증
    S->>E: 3. 작업 등록
    Note over E: XML 저장
    C->>S: 4. 작업 실행 요청
    S->>E: 5. 트리거 확인
    E->>R: 6. 실행 명령
    R->>P: 7. 프로세스 생성
    P-->>R: 8. 실행 결과
    R-->>S: 9. 상태 업데이트
```

## 명령 예시

```text
schtasks /create /tn "TaskName" /tr "command" /sc once /st HH:MM
schtasks /create /s remote-pc /u username /p password /tn "TaskName" /tr "command" /sc once /st HH:MM
schtasks /run /tn "TaskName"
schtasks /delete /tn "TaskName" /f
```

## 탐지 포인트

- `Microsoft-Windows-TaskScheduler/Operational` 이벤트 `106`, `200`, `201`
- `C:\Windows\System32\Tasks\` 신규 XML 작업 파일
- `schtasks.exe` 원격 옵션 `/s`, `/u`, `/p`
- 작업 실행 직후 비정상 자식 프로세스 생성

## 대응 방안

1. 원격 작업 생성 권한을 관리 서버와 관리자 계정으로 제한합니다.
2. 예약 작업 생성 이벤트를 모니터링합니다.
3. 시작 시 실행, 로그온 시 실행 같은 지속성 트리거를 주기적으로 점검합니다.

## 참고자료

- [Task Scheduler](https://learn.microsoft.com/ko-kr/windows/win32/taskschd/task-scheduler-start-page)
- [Schtasks.exe](https://learn.microsoft.com/ko-kr/windows/win32/taskschd/schtasks)
