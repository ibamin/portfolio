# Qilin Ransomware로 확인하는 Ransomware Trend

## 개요

| 항목 | 내용 |
|------|------|
| **분석 대상** | Qilin Ransomware (RaaS) |
| **공격 유형** | 3세대 랜섬웨어 — 다중 갈취 + 공급망 공격 |
| **피해 사례** | 2025.09 국내 금융권 MSP 침해 → 28개 이상 금융사 동시 감염 |
| **핵심 기법** | SafeBoot 모드 전환, VSS 삭제, 메모리 기반 암호화 |
| **Cheiron 시나리오** | `[Malware Emulation] Qilin Ransomware TTPs (2025-10)` |

**중요:** 본 문서에서 소개하는 공격 기법은 공개된 보안 분석 자료를 기반으로 한 일반적인 랜섬웨어 행위 패턴입니다. **Cheiron 시뮬레이션**은 실제 악성코드를 사용하지 않고, MITRE ATT&CK 프레임워크 기반으로 동일한 전술과 기법을 안전하게 재현합니다.

---

## 랜섬웨어 공격 트렌드의 변화

**1단계: 단순 암호화 (2010년대)**
- 파일 암호화 후 복호화 키 제공
- 백업으로 복구 가능

**2단계: 이중 갈취 (2019-2022)**
- 데이터 탈취 + 암호화
- 백업이 있어도 데이터 유출 협박

**3단계: 다중 갈취 및 공급망 공격 (2023-현재)**
- **삼중 갈취**: 암호화 + 데이터 유출 + DDoS/고객 협박
- **공급망 공격**: MSP, 파일 전송 솔루션 침해로 다수 기업 동시 감염
- **백업 시스템 파괴**: 복구 옵션 원천 차단
- **암호화 없는 갈취**: 데이터 탈취만으로 협박 (2025년 전체 공격의 6%)

Qilin Ransomware는 3단계에 해당하며, MSP 침해를 통해 28개 이상의 국내 금융사를 동시에 감염시킨 사례로 그 위협성이 입증되었습니다.

---

## 국내 금융권 공급망 공격 사례 (2025년 9월)

### 공격 개요

- **피해 기업**: 28개 이상의 국내 자산운용사 및 금융회사
- **공격 경로**: Managed Service Provider (MSP) 시스템 침해
- **공격 그룹**: Qilin Ransomware (RaaS)
- **피해 유형**: 랜섬웨어 감염, 데이터 유출, 서비스 중단

### 공격 프로세스

```
1. MSP 시스템 초기 침투 (피싱 또는 취약점 악용 추정)
2. MSP 내부 네트워크 정찰 및 권한 상승
3. MSP가 관리하는 고객사 접근 권한 탈취
4. 28개 금융사 시스템에 동시 접근
5. 각 금융사의 중요 데이터 탈취
6. Qilin Ransomware 배포 및 암호화
   - SafeBoot 모드 강제 전환
   - VSS 백업 삭제
   - 네트워크 백업 서버 암호화
7. 다크웹 유출 사이트에 피해 기업 정보 공개
```

### 시사점

- **공급망 내 단일 장애 지점(Single Point of Failure)**: MSP 하나의 침해로 다수 기업 동시 피해
- **제3자 위험 관리 필요성**: 외부 서비스 제공자에 대한 지속적인 보안 감사
- **접근 권한 최소화**: MSP가 고객사에 대해 가지는 권한을 최소화하고 모니터링 강화

---

## 공격 기법 상세 분석

---

### 1. Boot Mode Detection (부팅 모드 탐지)

많은 랜섬웨어들은 Windows의 SafeBoot 모드 특성을 악용합니다. SafeBoot 모드에서는 ntoskrnl.exe 드라이버 로더가 최소한의 드라이버만 로드하며, **EDR, AV, XDR의 드라이버가 로드되지 않습니다**.

일반적인 공격 흐름:
1. 현재 시스템의 부팅 모드 확인 (레지스트리 쿼리)
2. 정상 모드일 경우 SafeBoot 모드로 전환 시도
3. 시스템 재부팅 후 보안 솔루션 우회 상태에서 암호화 수행

**탐지 포인트:**
- SafeBoot 관련 레지스트리 쿼리 탐지
- bcdedit 명령어를 통한 부팅 설정 변경 모니터링
- 비정상적인 SafeBoot 모드 진입 알림

**Cheiron 재현:** "Boot Mode Detection using reg query" — T1082

---

### 2. Volume Shadow Copy 삭제

랜섬웨어는 백업 복구를 방지하기 위해 Windows의 Volume Shadow Copy Service(VSS)를 파괴합니다:

1. VSS 서비스를 수동 실행으로 변경 (자동 백업 생성 방지)
2. 모든 볼륨 섀도우 복사본 삭제
3. VSS 서비스 종료 및 비활성화

**탐지 포인트:**
- vssadmin.exe 프로세스 실행 모니터링
- VSS 서비스 상태 변경 감지
- Shadow Copy 삭제 이벤트 로그 (Event ID 524)

**Cheiron 재현:** "Delete created Volume Shadow Copy using vssadmin.exe" — T1490

---

### 3. Persistence (지속성 확보)

**주요 기법:**
1. **Registry Run Keys (T1547.001)**: 레지스트리 Run 키에 악성코드 경로 등록
2. **Scheduled Task (T1053.005)**: Windows 작업 스케줄러에 예약 작업 생성

**탐지 포인트:**
- Run 키 레지스트리 변경 모니터링 (HKLM/HKCU)
- schtasks.exe 프로세스의 비정상적인 작업 생성 탐지
- 시작 프로그램 폴더 변경 감지

---

### 4. Lateral Movement (측면 이동)

랜섬웨어는 네트워크 내 다른 시스템으로 확산하여 피해 범위를 확대합니다.

**주요 기법:**
- RDP(Remote Desktop Protocol)를 통한 원격 접속
- 탈취한 자격증명을 활용한 인증
- 연결된 시스템에 악성코드 복사 및 실행

**탐지 포인트:**
- 비정상적인 RDP 연결 시도 모니터링
- cmdkey.exe를 통한 자격증명 저장 탐지
- 짧은 시간 내 다수 시스템으로의 RDP 연결 패턴 분석

**Cheiron 재현:** "Exploitation of Remote Services via RDP" — T1021.001

---

### 5. Discovery (정찰)

**주요 정찰 활동:**
1. **시스템 정보 수집**: CPU, 메모리, 사용자 정보 파악
2. **드라이브 탐색**: 로컬 및 네트워크 드라이브 식별
3. **파일 탐색**: 암호화 대상 파일 목록 생성
4. **네트워크 공유 조회**: 네트워크 드라이브 및 공유 폴더 탐색

**탐지 포인트:**
- Windows Native API 호출 패턴 모니터링
- 대량 파일 탐색 행위 탐지
- net.exe를 통한 네트워크 조회 탐지

**Cheiron 재현:**
- "System Information Discovery via GetSystemInfo API" — T1082
- "System Network Connections Discovery" — T1135

---

### 6. Defense Evasion (탐지 회피)

**주요 회피 기법:**
1. **레지스트리 조작 (T1112)**: 네트워크 드라이브 접근 권한 확대, 심볼릭 링크 활성화
2. **이벤트 로그 삭제 (T1070.001)**: 공격 증거 제거

**탐지 포인트:**
- 레지스트리 정책 변경 모니터링 (EnableLinkedConnections, SymlinkEvaluation)
- wevtutil.exe를 통한 이벤트 로그 삭제 탐지
- Event ID 1102 (로그 삭제 이벤트) 모니터링

---

### 7. Impact (영향)

#### 7.1 파일 암호화 (T1486)

**Qilin Ransomware 암호화 특징:**
- **Rust 기반 크로스 플랫폼**: Windows, Linux, ESXi 환경 모두 지원
- **적응형 암호화 알고리즘**:
  - AES-NI 지원 CPU: **AES-CTR** 알고리즘 사용
  - AES-NI 미지원 CPU: **ChaCha20** 알고리즘 사용
  - **RSA-4096**으로 대칭키 암호화 (복호화 불가능)
- **Intermittent Encryption**: 파일 전체가 아닌 일부 블록만 암호화하여 속도 향상
- **멀티스레딩**: 시스템 리소스를 최대한 활용한 고속 암호화

**탐지 포인트:**
- 대량 파일 I/O 작업 모니터링
- 파일 확장자 일괄 변경 탐지
- 비정상적인 CPU 사용률 증가 패턴

#### 7.2 Wallpaper Defacement (T1491.001)

감염 사실을 즉각 알리고 심리적 압박을 가하기 위해 사용자 바탕화면을 협박 메시지로 변경합니다.

---

## Cheiron 시뮬레이션 시나리오

### Attack Flow

```
[초기 침투]
├─ Download Qilin Ransomware (2025-10)
└─ Load Memory

[정찰 및 탐지]
├─ Boot Mode Detection using "reg query"
├─ System Information Discovery via GetSystemInfo API
├─ System Info Discovery via GlobalMemoryStatusEx API
├─ System Owner/User Discovery via GetUserNameW API
├─ Logical Drives Discovery via GetLogicalDrives API
├─ Drive Type Discovery via GetDriveTypeW API
├─ File Discovery via FindFirstFileW and FindNextFileW API
├─ System Network Connections Discovery
├─ EnableLinkedConnections SMB Access Enablement
└─ SymlinkEvaluation Registry Manipulation

[백업 파괴]
└─ Delete Volume Shadow Copy using vssadmin.exe

[지속성 확보]
├─ Persistence Through Registry Run Keys
└─ Persistence Through Scheduled Task

[측면 이동]
└─ Exploitation of Remote Services via RDP

[탐지 회피]
└─ Windows Event Log Deletion via wevtutil.exe

[영향]
├─ Download Encryption Module
├─ Execute Encryption Module on Memory
├─ Download qilin Wallpaper
└─ Set User Wallpaper Through Registry
```

### 주요 절차 (25 Procedures)

| 절차 이름 | 설명 | MITRE Technique |
|----------|------|-----------------|
| Download Qilin Ransomware (2025-10) | 랜섬웨어 다운로드 | T1105 |
| Boot Mode Detection using "reg query" | SafeBoot 모드 탐지 | T1082 |
| Delete Volume Shadow Copy | VSS 백업 삭제 | T1490 |
| Persistence Through Registry Run Keys | Run 키 등록 | T1547.001 |
| Persistence Through Scheduled Task | 예약 작업 생성 | T1053.005 |
| Exploitation of Remote Services via RDP | RDP 측면 이동 | T1021.001 |
| System Information Discovery | 시스템 정보 수집 | T1082 |
| Network Share Discovery | 네트워크 공유 탐색 | T1135 |
| File Discovery via Native API | 파일 탐색 | T1083 |
| Windows Event Log Deletion | 로그 삭제 | T1070.001 |
| Execute Encryption Module on Memory | 메모리 기반 암호화 | T1486 |
| Set User Wallpaper Through Registry | 배경화면 변경 | T1491.001 |

### 시뮬레이션 활용 방안

**EDR/XDR 탐지 능력 검증:**
- SafeBoot 모드 전환 탐지
- VSS 삭제 명령어 탐지
- 비정상적인 레지스트리 수정 탐지
- 메모리 기반 악성 스크립트 실행 탐지
- 대량 파일 암호화 행위 탐지

**네트워크 보안 검증:**
- C2 통신 탐지
- 데이터 유출 탐지
- Lateral Movement 탐지

---

## MITRE ATT&CK Mapping

| Tactic | Technique ID | Technique Name | Qilin 구현 |
|--------|--------------|----------------|------------|
| Initial Access | T1078 | Valid Accounts | MSP 자격증명 탈취 |
| Execution | T1059.001 | PowerShell | 메모리 기반 암호화 스크립트 |
| Persistence | T1547.001 | Registry Run Keys | HKCU\...\Run 등록 |
| Persistence | T1053.005 | Scheduled Task | schtasks /create |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | 취약점 악용 (추정) |
| Defense Evasion | T1562.001 | Impair Defenses | SafeBoot 모드 전환 |
| Defense Evasion | T1070.001 | Clear Windows Event Logs | wevtutil cl |
| Defense Evasion | T1112 | Modify Registry | SymlinkEvaluation, EnableLinkedConnections |
| Discovery | T1082 | System Information Discovery | GetSystemInfo, GlobalMemoryStatusEx |
| Discovery | T1083 | File and Directory Discovery | FindFirstFileW, FindNextFileW |
| Discovery | T1135 | Network Share Discovery | net use |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | cmdkey + mstsc |
| Impact | T1486 | Data Encrypted for Impact | In-Memory 암호화 모듈 |
| Impact | T1490 | Inhibit System Recovery | vssadmin delete shadows |
| Impact | T1491.001 | Internal Defacement | 배경화면 변경 |

---

## 참고자료

1. [SOMANSA — Qilin Ransomware 분석](https://www.somansa.com/ko/security-report/security-note/qilin_ransomware/)
2. [AhnLab ASEC — Qilin Ransomware 기술 분석](https://asec.ahnlab.com/en/90497/)
3. [MITRE ATT&CK Framework](https://attack.mitre.org/)
4. [CISA Ransomware Guide](https://www.cisa.gov/)
5. [Ransomware Live Tracker](https://ransomware.live/)
6. 금융보안원 — 2025년 금융권 랜섬웨어 공격 사례 보고서
7. [TrendMicro — New Golang Ransomware Agenda](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
8. [TrendMicro — Agenda Ransomware Uses Rust](https://www.trendmicro.com/en_us/research/22/l/agenda-ransomware-uses-rust-to-target-more-vital-industries.html)
9. [Group-IB — Qilin Revisited](https://www.group-ib.com/blog/qilin-revisited/)
10. [Cisco Talos — Uncovering Qilin Attack Methods](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
