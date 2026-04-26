# BAS-Simulation
## 구조 다이어그램

```mermaid
flowchart LR
    Hypothesis["시나리오 가설"] --> Emulation["공격 에뮬레이션"]
    Emulation --> Telemetry["로그 수집"]
    Telemetry --> Detection["탐지 검증"]
    Detection --> Hardening["개선/하드닝"]
```


BAS 기반 공격 시나리오 및 자동화 자산을 정리합니다.

## Scenarios
- [Visual Studio 취약점 기반 개발 인프라 감염 시나리오](Scenarios/Scenario-Visual-Studio-Infection.md)
- [CIS Benchmark 점검 시나리오](Scenarios/Scenario-CIS-Benchmark-Audit.md)
- [Qilin SafeMode 우회 시나리오](Scenarios/Scenario-Qilin-SafeMode.md)
- [SideWinder DLL Sideloading 시나리오](Scenarios/Scenario-SideWinder-DLL-Sideloading.md)
- [Git Credential 탈취 탐지 시나리오](Scenarios/Scenario-Git-Credential-Theft.md)
