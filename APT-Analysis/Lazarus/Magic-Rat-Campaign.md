# Lazarus Magic Rat Campaign (분석 요약)

## Overview
- **기간**: 2024-10-18 → 2024-10-31
- **소속**: SOMMA
- **기여도**: 100%
- **초기 침투**: VMware Horizon 환경에서 Log4Shell(CVE-2021-44228) 악용

## Attack Flow (요약)
- **Initial Access**: Log4Shell로 Reverse Shell 획득
- **Execution**: Magic RAT 다운로드 및 실행
- **Discovery**: Windows/Linux 환경 정보 수집
- **Persistence**:
  - Windows: Scheduled Task/Startup 등록
  - Linux: crontab, systemd 서비스 등록
- **Actions on Objectives**: 랜섬웨어, 자료 조사/유출 등

## Key TTPs
- 시스템/계정 정보 수집
- 포트 스캐너(이미지 위장) 다운로드
- 추가 RAT(Tiger Rat) 다운로드

## IOCs (요약)
- **Hashes**: Magic RAT, Tiger RAT, Port Scanner 해시 다수
- **C2 URL**: `hxxp[://]64.188.27.73/...` 등
- **IPs**: 193.56.28.251, 52.202.193.124, 64.188.27.73, 151.106.2.139, 66.154.102.91

## Mitigation
- Log4j 보안 업데이트 적용
- 외부 노출 VMware Horizon 환경 점검

## References
- Talos Lazarus MagicRat 분석
- Log4j 보안 권고
