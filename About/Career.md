# Career Highlights
## 구조 다이어그램

```mermaid
flowchart LR
    Profile["Career Highlights"] --> Experience["경력과 역할"]
    Experience --> Skills["보안 역량"]
    Skills --> Evidence["프로젝트 증거"]
    Evidence --> Direction["지원 방향"]
```


## 주요 프로젝트 1 — OilRig 내부 관계 기반 DB 백업 유출 시나리오
**목표**: 내부망 침투 후 DB 백업 파일 탈취 시나리오 설계
- **Initial Access**: Spear phishing 악성 .docm 실행
- **Discovery**: Vaultcmd 통한 Windows Credential Manager 확인, RDP 접속 여부 레지스트리 조회
- **Credential Access**: Windows Credential Manager 자격 증명 추출, Mimikatz로 LSASS 메모리 덤프
- **Credential Cracking**: 추출한 자격증명 패스워드 정규화
- **Lateral Movement**: IIS WebShell 사용, RDP 원격 접속
- **Persistence**: Plink 포트 포워딩으로 내부 서버 접근 유지
- **Discovery**: DB 서버 Backup 파일 탐색
- **Exfiltration**: Windows Exchange API 기반 유출

## 주요 프로젝트 2 — Lazarus 그룹정책 / PMS 기반 인프라 장악 시나리오
**목표**: 도메인 정책을 통한 인프라 장악 시나리오 설계
- **Initial Access**: Spear phishing 악성 .docm 실행
- **Discovery**: Credentials 경로 기반 RDP 자격증명 존재 여부 확인
- **Privilege Escalation**: Fodhelper UAC Bypass
- **Credential Access**: 자격증명 GUID 값 복호화, Pktmon/Tcpdump 패킷 덤핑
- **Credential Cracking**: 패스워드 정규화
- **Lateral Movement**: WinRM + Python 프록시, ngrok 통한 리버스 쉘 제어
- **Persistence**: 스케줄러/도메인 정책 기반 지속성 유지
- **Discovery**: LDAP 기반 도메인 정책 조회
- **Impact**: 다운로더 자동 실행 정책 생성 및 배포

## 주요 프로젝트 3 — Visual Studio 취약점 기반 개발 인프라 감염 시나리오
**목표**: 개발 인프라 침투 및 랜섬웨어 단계까지 시뮬레이션
- **Initial Access**: 유출된 WebHook을 통한 악성 Visual Studio 프로젝트 다운로드/실행 유도
- **Discovery**: 로컬 네트워크/도메인 환경 정보 수집
- **Privilege Escalation**: CVE-2024-20656 활용 NT\SYSTEM 권한 획득
- **Credential Access**: Mimikatz로 LSASS 덤프, Chrome Login Data 접근
- **Exfiltration**: 자격증명 유출
- **Lateral Movement**: CreateProcessWithLogonW WinAPI 기반 리버스 쉘
- **Defense Evasion**: COM 객체 활용 정상 인스턴스 생성, Reflective Injection
- **Persistence**: HKCU\Software\Microsoft\Windows\CurrentVersion\Run 등록
- **Discovery**: 내부망 타겟 여부 판단 정보 수집
- **Impact**: 랜섬웨어 단계 시뮬레이션

## 주요 프로젝트 4 — CIS Benchmark 점검 시나리오
- CIS Benchmark 기준 항목을 점검/자동화하는 시나리오 설계 및 시뮬레이션

---

---

## SOMMA 주요 성과 (RedBlue 주임연구원, 2024.01 ~ 재직 중)

**주요 업무:** 보안 설정 점검 자동화 도구 개발, 행위 기반 탐지 정책 설계/검증, APT/랜섬웨어 TTP 분석 및 공격 시뮬레이션, 보안 테스트 인프라 구축/운영

### 1. 보안 점검 자동화 도구 개발

PoC 및 BAS 테스트 환경 세팅 시 하드닝 점검을 수동으로 진행하며 2~3시간 소요, 담당자마다 누락 항목이 달랐던 문제를 해결하기 위해 CIS Benchmark 기반 점검 CLI 도구를 직접 개발.

**Apache / Ubuntu 점검 (Python/Bash)**
- CIS Apache Secure Benchmark 기반 Module 설정, 파일 권한, Access Policy, SSL/TLS 설정 자동 점검
- 각 항목을 독립 함수로 모듈화, 시스템 명령 출력 파싱해 Pass/Fail/Manual 자동 분류
- JSON/HTML 리포트 자동 생성, 팀 전체 동일 기준 점검 표준화

**Windows Server 2019 점검 (PowerShell)**
- Account/Local Policies, Event Log 정책, Registry 키 설정, Firewall 정책, Public Key Policies 자동 점검 (50+ 항목)
- 점검 소요 시간 2~3시간 → 약 1시간으로 단축, 팀 내 재사용률 95% 이상
- 현재 PoC 사전 환경 점검 표준 도구로 팀 전체 운영 중

### 2. 취약점 기반 탐지 정책 설계 및 검증

공격 시나리오 개발과 탐지 정책 설계를 병행하며 Sigma Rule 40+를 개발해 자사 EDR(Cheiron)에 연동/검증.

**Git Credential 탈취 탐지 (T1552.001)**
- `git config credential.helper store` 설정이 기존 EDR에서 전혀 탐지되지 않는 것을 발견
- Windows (Sysmon EventID 1) / Linux (auditd) 양쪽 탐지 규칙 설계
- 탐지 커버리지 0% → 100%, FP 2건 제거, Cheiron EDR + SIEM Alert Mapping 연동 완료

**Qilin 랜섬웨어 Safe Mode 우회 탐지 (T1562.009)**
- bcdedit → Safe Mode 재부팅 → EDR 비활성화 → 랜섬웨어 실행 체인 분석
- 두 이벤트 순차 발생을 Correlation Rule로 묶어 High Severity 에스컬레이션 설계
- Qilin BAS 시나리오 탐지율 100%, BlackMatter/AvosLocker 유사 기법에도 동일 규칙 적용 확인

### 3. 취약점 분석 및 PoC 재현

공개 PoC 기반 실험 환경 재현, 공격 성공 조건과 탐지 가능 아티팩트 분석 후 자산화.

- **CVE-2024-38063** (CVSS 9.8, Windows TCP/IP IPv6 RCE): 공격 성공 조건 및 네트워크 이상 패턴/행위 로그 자산화
- **CVE-2024-20656** (Visual Studio): .suo 역직렬화 → NT\SYSTEM 권한 취득 → Reflective Injection 백도어 체인 재현
- **Qilin 랜섬웨어** (Rust 기반, AES-256-GCM + RSA-2048): Ghidra/x64dbg로 정적/동적 분석, YARA/Sigma Rule 생성
- **SideWinder APT** DLL Sideloading (vsstrace.dll): ConfuserEx 난독화, 외부 OLE 객체 주입 패턴 분석

### 4. 보안 자동화 도구 개발 및 인프라 운영

**내부 보안 도구 개발 (Python / Rust / C++)**
- Banner Scraper: 서비스 배너/버전 자동 수집, 취약 버전 식별 자동화
- Packet Generator: 커스텀 패킷 생성/전송, 네트워크 취약점 검증용
- AD 내부 정찰 도구: LDAP API 직접 활용, 도메인 사용자/그룹/OU 열거 및 Trust 관계 매핑 (Windows/Linux 크로스 빌드)
- Excel-to-Cheiron 템플릿 변환 도구: API 연동, 수작업 제거로 팀 운영 효율 개선
- Malware Dropper: 시나리오용 페이로드 드롭퍼, Python/Rust 기반

**Hyper-V 기반 8VM 격리 테스트 인프라 구축/운영**
- 구성: AD DC(Alpha), 파일서버/MSSQL(Bravo), Exchange+Web(Charlie), Linux 서버(Delta), 워크스테이션(Echo/Foxtrot/Golf), 공격자 머신(Kali)
- 스냅샷 기반 초기 상태 관리로 재현 실패율 최소화, Docker로 취약 서비스 격리 배포
- 권한/패키지/네트워크 조건 체크리스트를 표준화해 팀 공통 워크플로우로 채택

### 5. 기술 블로그 운영

- MITRE ATT&CK 14개 Tactic 기반 공격 기법별 분석 문서 작성
- 개요 → 동작 방식 → 실습 → 탐지(Sigma Rule) → 대응 방안 체계로 정리
- [Tech Blog 바로가기](/TechBlog/README.md)

---

## 프로젝트 요약

### Lazarus Magic Rat Campaign 분석 보고서
- **유형**: 모의 해킹 / 분석 보고서
- **소속**: SOMMA
- **기여도**: 100%
- **기간**: 2024-10-18 → 2024-10-31
- **설명**: Lazarus 캠페인 흐름을 분석하고 시뮬레이션 관점에서 정리

### Signature Based HIDS (졸업프로젝트)
- **유형**: AI 기반 보안 분석
- **소속**: 호서대학교 팀프로젝트
- **기여도**: 35%
- **기간**: 2023-03-08 → 2023-10-08
- **스택**: AI, Node.js, Python, Windows
- **설명**: 공개 악성 패킷 데이터셋을 활용한 시그니처 기반 HIDS 설계

### 웹 사이트 모의해킹 보고서
- **유형**: 모의 해킹 보고서
- **소속**: 한국정보보호 교육센터
- **기간**: 2022-11-23 → 2022-11-30
- **설명**: 취약점 탐지 및 보고서 작성 실습
