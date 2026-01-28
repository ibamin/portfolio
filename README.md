# Security Research & Defense Portfolio

APT 분석, 취약점 리서치, BAS(Breach & Attack Simulation) 시나리오를 통해  
**공격을 이해하고 재현하여 방어 가능한 보안 자산으로 전환**하는 것을 목표로 합니다.

---

## About (Summary)

**노경록 | Security Threat Analyst**  
APT 공격 시나리오 분석/자동화, 1-Day 취약점 PoC 검증 및 리팩토링, CIS Benchmark 점검 자동화를 수행했습니다.  
실전 환경에서 재현 가능한 시뮬레이션 자산을 구축하고, 공격 흐름을 방어 관점의 문서로 전환하는 데 강점이 있습니다.

- **현 직장**: 쏘마(Somma) RedBlue 연구원 (2024.01 ~ 재직 중)
- **핵심 역량**: APT 시나리오 자산화, PoC 검증/자동화, BAS 시뮬레이션 설계
- **관심 분야**: Offensive Security, 공격 시뮬레이션, 탐지/대응 연계

자세한 이력과 경력 요약은 `About` 섹션에서 확인할 수 있습니다.

---

## Portfolio (Notion Export 기반)

Notion 포트폴리오 PDF 내보내기 데이터를 기준으로 프로젝트/스킬/CVE 리포트를 정리했습니다.

- [Projects](Portfolio/Projects.md)
- [Skills](Portfolio/Skills.md)
- [CVE Highlights](Portfolio/CVE-Highlights.md)

---

## What I Focus On

### APT Analysis
- Lazarus, Kimsuky, Andariel, OilRig 등 APT 그룹 분석
- MITRE ATT&CK 기반 TTP 정리
- 단발 공격이 아니라 **캠페인 시나리오 관점**으로 분석

### BAS (Breach & Attack Simulation)
- APT/취약점 기반 공격 시나리오 설계
- 방어 관점에서 재현 가능한 테스트 시나리오 구축
- 자동화 스크립트 및 실행 파일 형태의 자산화

### Vulnerability Research
- 1-Day 취약점 분석/PoC 검증
- Root Cause / Attack Flow / Simulation / Mitigation / Detection 중심 문서화
- 취약점을 보안 점검/시뮬레이션 자산으로 전환

---

## Featured Scenarios

### APT-Analysis
- [OilRig DB 백업 유출 시나리오](APT-Analysis/OilRig/Scenario-DB-Backup-Exfil.md)
- [Lazarus 도메인 정책 기반 인프라 장악 시나리오](APT-Analysis/Lazarus/Scenario-Domain-Policy-PMS.md)

### BAS-Simulation
- [Visual Studio 취약점 기반 개발 인프라 감염 시나리오](BAS-Simulation/Scenarios/Scenario-Visual-Studio-Infection.md)
- [CIS Benchmark 점검 시나리오](BAS-Simulation/Scenarios/Scenario-CIS-Benchmark-Audit.md)

---

## Repository Structure

```text
portfolio-root
├─ About               # 이력/경력/자기소개
├─ Portfolio           # Notion export 기반 요약
├─ APT-Analysis        # APT 그룹별 분석 및 캠페인 정리
├─ BAS-Simulation      # 공격 시나리오 기반 시뮬레이션
├─ CVE-Research        # 취약점 분석 및 방어 관점 문서
├─ Tools               # 분석/자동화를 위한 보조 도구
└─ docs                # 학습/기록 문서
```
