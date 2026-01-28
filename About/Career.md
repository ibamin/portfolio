# Career Highlights

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
