# Lazarus 도메인 정책 기반 인프라 장악 시나리오

## 개요
Lazarus 그룹의 공격 흐름을 가정하여, 그룹 정책과 PMS를 활용한 인프라 장악 과정을 재현하는 시나리오입니다.

## 목표
- 초기 침투 후 자격증명 확보 및 권한 상승 경로 검증
- 도메인 정책을 이용한 지속성/확산 흐름 재현
- 다운로더 배포 및 장악 단계 검증

## 공격 흐름 (TTP)
- **Initial Access**: Spear phishing 악성 `.docm` 실행
- **Discovery**: `$env:userprofile\appdata\Local\Microsoft\Credentials` 기반 RDP 자격증명 존재 여부 확인
- **Privilege Escalation**: Fodhelper UAC Bypass
- **Credential Access**: Credentials GUID 기반 복호화, Pktmon/Tcpdump 패킷 덤핑
- **Credential Cracking**: 패스워드 정규화
- **Lateral Movement**: WinRM + Python 프록시, ngrok 통한 리버스 쉘 제어, 공유 폴더로 다운로더 전송
- **Persistence**: 스케줄러 및 도메인 정책 기반 지속성 유지
- **Discovery**: LDAP 기반 도메인 정책 조회
- **Impact**: 다운로더 자동 실행 정책 생성/배포

## 시뮬레이션 관점 포인트
- 도메인 정책 변경 이벤트 추적
- WinRM/프록시 기반 lateral movement 탐지
- 스케줄러 및 정책 기반 지속성 유지 신호
- 다운로더 배포/실행 행위 모니터링
