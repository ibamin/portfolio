# Andariel (Silent Chollima / Plutonium)

## 개요

| 항목 | 내용 |
|------|------|
| **활동 시기** | 2009년 ~ 현재 |
| **소속** | 북한 정찰총국 3국 (Lazarus 하위 그룹) |
| **표적 지역** | 한국 (주요), 일본, 인도, 동남아시아 |
| **표적 섹터** | 국방, 방산, 에너지, 의료, 금융, IT |
| **공격 목적** | 군사/국방 정보 수집, 금전 탈취 (랜섬웨어) |
| **주요 기법** | 한국 소프트웨어 취약점 악용, 워터링홀, 커스텀 RAT |

---

## 캠페인 특성

Andariel은 Lazarus 그룹의 하위 조직으로, **한국의 국방/방산 분야를 집중적으로 표적**합니다. 한국에서 널리 사용되는 소프트웨어(HWP, ActiveX, 공인인증서 관련 S/W)의 취약점을 적극 악용하며, 최근에는 **랜섬웨어(Maui)**를 통한 금전 탈취로 활동 범위를 확장하고 있습니다.

**특징적 패턴:**
- **한국 특화 소프트웨어** 취약점 악용 (HWP 문서, ActiveX, VPN 솔루션)
- 방산 업체 대상 **워터링홀 공격** — 방산 관련 웹사이트 변조
- **공급망 공격** — IT 관리 솔루션, 보안 소프트웨어 업데이트 서버 침해
- 최근 **Maui 랜섬웨어**로 의료/에너지 분야 금전 탈취
- 초기 침투 후 수개월간 잠복하며 정보 수집 (Low and Slow)

---

## 주요 악성코드

| 악성코드 | 유형 | 설명 |
|----------|------|------|
| **Andarat** | Custom RAT | 초기 정찰/제어용 백도어 |
| **TigerRAT** | Backdoor | 파일 관리, 키로깅, 스크린샷, C2 통신 |
| **NukeSped** | Backdoor | 다기능 백도어 (Lazarus 계열 공유) |
| **Maui** | Ransomware | 수동 실행형 랜섬웨어 (AES-128-CBC + RSA) |
| **DTrack** | Spyware | 키로깅, 브라우저 히스토리, 프로세스 정보 수집 |
| **EarlyRAT** | RAT | Log4Shell 취약점 통한 초기 접근 후 배포 |

---

## 공격 흐름

```
[Initial Access]
  Case A: 한국 S/W 취약점 악용 (HWP, ActiveX, VPN)
  Case B: 워터링홀 — 방산/국방 관련 웹사이트 변조
  Case C: Spearphishing — 방산/국방 관련 문서 위장
  Case D: 공급망 — IT 관리 솔루션 업데이트 서버 침해
      ↓
[Execution — T1059, T1203]
  취약점 트리거 → 셸코드 실행 → 1차 로더 드롭
      ↓
[Persistence — T1547.001, T1543.003]
  Registry Run Key / Windows 서비스 등록
      ↓
[Defense Evasion — T1027, T1036]
  DLL Side-Loading, 정상 프로세스 위장
      ↓
[Discovery — T1082, T1083, T1049]
  시스템/네트워크/파일 정보 수집
  Active Directory 정찰 (도메인 환경)
      ↓
[Credential Access — T1003.001]
  Mimikatz / 자격증명 덤프
      ↓
[Lateral Movement — T1021.001, T1021.002]
  RDP / SMB 기반 횡이동
      ↓
[Collection — T1005, T1039]
  방산/국방 관련 문서 수집
  네트워크 공유 파일 수집
      ↓
[Exfiltration — T1041, T1048]
  C2 채널 또는 별도 채널로 데이터 유출
      ↓
[Impact (선택적)]
  Maui 랜섬웨어 배포 — 금전 탈취 목적
```

---

## 주요 TTP (MITRE ATT&CK)

| Tactic | Technique ID | Technique Name | Andariel 구현 |
|--------|--------------|----------------|--------------|
| Initial Access | T1190 | Exploit Public-Facing Application | 한국 S/W 취약점, Log4Shell |
| Initial Access | T1189 | Drive-by Compromise | 워터링홀 공격 |
| Initial Access | T1195.002 | Supply Chain Compromise | IT 관리 솔루션 침해 |
| Execution | T1059.001 | PowerShell | 초기 로더, 정찰 스크립트 |
| Execution | T1203 | Exploitation for Client Execution | HWP/ActiveX 취약점 |
| Persistence | T1547.001 | Registry Run Keys | 자동 실행 등록 |
| Persistence | T1543.003 | Windows Service | 서비스 등록 기반 지속성 |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | 로컬 권한 상승 취약점 |
| Defense Evasion | T1574.002 | DLL Side-Loading | 정상 바이너리 악용 |
| Defense Evasion | T1027 | Obfuscated Files | 페이로드 난독화/암호화 |
| Defense Evasion | T1036 | Masquerading | 정상 프로세스명 위장 |
| Credential Access | T1003.001 | LSASS Memory Dump | Mimikatz 활용 |
| Discovery | T1082 | System Information Discovery | 시스템 정보 수집 |
| Discovery | T1049 | System Network Connections | 네트워크 연결 정보 |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | RDP 횡이동 |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | 네트워크 공유 전파 |
| Collection | T1005 | Data from Local System | 방산/기밀 문서 수집 |
| Collection | T1039 | Data from Network Shared Drive | 공유 드라이브 수집 |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | C2 채널 유출 |
| Impact | T1486 | Data Encrypted for Impact | Maui 랜섬웨어 |

---

## 탐지 포인트

### 초기 접근
- 한국 특화 소프트웨어(`hwp.exe`, ActiveX 컨트롤)에서 비정상 자식 프로세스 생성
- 워터링홀 관련 도메인/IP 차단 (방산 관련 사이트 변조 이력 모니터링)
- IT 관리 솔루션 업데이트 서버의 비정상 파일 배포 탐지

### 엔드포인트
- `svchost.exe` 위장 프로세스 (비정상 경로에서 실행)
- `%ProgramData%`, `%PUBLIC%` 경로에서 DLL/EXE 실행
- Mimikatz 관련 LSASS 접근 패턴 (Sysmon EventID 10)
- Registry Run Key 변경 모니터링

### 네트워크
- 비표준 포트를 통한 HTTP/HTTPS 통신
- 내부 네트워크 스캔 패턴 (짧은 시간 내 다수 IP/포트 접근)
- 대용량 파일 외부 전송 탐지

---

## 참고자료

1. [MITRE ATT&CK — Andariel](https://attack.mitre.org/groups/G0138/)
2. [CISA — North Korean Maui Ransomware](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-187a)
3. [AhnLab ASEC — Andariel 분석](https://asec.ahnlab.com/ko/tag/andariel/)
4. [Kaspersky — Andariel's Mistakes](https://securelist.com/andariel-mistakes/107254/)
5. [KISA — 북한 사이버 위협 동향](https://www.boho.or.kr/)
