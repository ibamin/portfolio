# OilRig DB 백업 유출 시나리오

## 개요
OilRig 그룹 내부 관계 기반 침투 후 DB 백업 파일을 탈취하는 시나리오입니다.  
초기 침투부터 자격증명 탈취, 내부 확장, 데이터 유출까지의 흐름을 재현합니다.

## 목표
- 스피어피싱 기반 초기 침투 경로 검증
- 자격증명 탈취/크랙 과정 재현
- 내부망 확장 및 DB 백업 파일 탐색
- Exfiltration 경로 검증

## 공격 흐름 (TTP)
- **Initial Access**: Spear phishing 악성 `.docm` 실행
- **Discovery**: Vaultcmd로 Credential Manager 조회, RDP 접속 여부 레지스트리 확인
- **Credential Access**: Credential Manager 자격증명 추출, Mimikatz로 LSASS 메모리 덤프
- **Credential Cracking**: 추출 패스워드 정규화
- **Lateral Movement**: IIS WebShell 로드/사용, RDP 원격 접속
- **Persistence**: Plink 포트 포워딩으로 내부 서버 접근 유지
- **Discovery**: DB 서버 Backup 파일 탐색
- **Exfiltration**: Windows Exchange API 기반 유출

## MITRE ATT&CK 매핑 (요약)
| Tactic | Technique |
| --- | --- |
| Initial Access | T1566.001 Spearphishing Attachment; T1204.002 User Execution: Malicious File |
| Discovery | T1012 Query Registry; T1083 File and Directory Discovery |
| Credential Access | T1555.004 Credentials from Password Stores: Windows Credential Manager; T1003.001 OS Credential Dumping: LSASS Memory |
| Credential Access | T1110 Brute Force (Password Cracking) |
| Lateral Movement | T1021.001 Remote Services: RDP; T1505.003 Server Software Component: Web Shell |
| Persistence | T1572 Protocol Tunneling (Port Forwarding) |
| Exfiltration | T1048 Exfiltration Over Alternative Protocol |

## 시뮬레이션 관점 포인트
- 자격증명 저장/관리 경로에 대한 탐지 로직
- LSASS 덤프 및 WebShell 행위 감지 시그널
- 백업 파일 접근/이동 로그 추적
- Exchange API 기반 외부 전송 모니터링
