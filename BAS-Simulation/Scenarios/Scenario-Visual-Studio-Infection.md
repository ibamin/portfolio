# Visual Studio 취약점 기반 개발 인프라 감염 시나리오

## 개요
유출된 WebHook을 이용해 악성 Visual Studio 프로젝트를 배포하고, 취약점(CVE-2024-20656)을 통해 NT\SYSTEM 권한을 획득하는 시나리오입니다.

## 목표
- 개발 환경에서의 초기 감염 경로 재현
- 권한 상승 및 자격증명 탈취 흐름 검증
- 내부망 확장 및 랜섬웨어 단계 시뮬레이션

## 공격 흐름 (TTP)
- **Initial Access**: 유출된 WebHook 기반 악성 VS 프로젝트 다운로드/실행 유도
- **Discovery**: 로컬 네트워크/도메인 환경 정보 수집
- **Privilege Escalation**: CVE-2024-20656 활용 NT\SYSTEM 권한 획득
- **Credential Access**: Mimikatz로 LSASS 덤프, Chrome Login Data 접근
- **Exfiltration**: 자격증명 유출
- **Lateral Movement**: CreateProcessWithLogonW WinAPI 기반 리버스 쉘
- **Defense Evasion**: COM 객체 활용 정상 인스턴스 생성, Reflective Injection
- **Persistence**: HKCU\Software\Microsoft\Windows\CurrentVersion\Run 등록
- **Discovery**: 내부망 타겟 여부 판단 정보 수집
- **Impact**: 랜섬웨어 단계 시뮬레이션

## 시뮬레이션 관점 포인트
- 개발자 환경(IDE/Build 경로) 기반 초기 감염 탐지
- 권한 상승 및 Mimikatz 행위 탐지
- COM/Reflective Injection 기반 은닉 행위 모니터링
- 랜섬웨어 단계 전후의 파일/프로세스 변화 추적
