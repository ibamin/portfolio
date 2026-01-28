# Security Research & Defense Portfolio

APT 분석, 취약점 리서치, BAS(Breach & Attack Simulation)를 통해  
**공격을 이해하고 시연하여 방어 가능한 보안 자산으로 전환하는 것**에 집중하는  
보안 엔지니어의 연구 및 실무 포트폴리오입니다.

---

## About This Portfolio

이 저장소는 단순한 코드 모음이 아니라, 다음 질문에 답하기 위해 정리된 포트폴리오입니다.

- 실제 APT 공격자는 어떤 흐름으로 침투하는가?
- 해당 공격은 **어디에서 탐지 가능했는가?**
- 취약점과 공격 기법을 **보안 점검 또는 시뮬레이션 자산으로 어떻게 전환할 수 있는가?**

모든 문서는 **분석 → 공격 흐름 이해 → 시뮬레이션 → 방어/탐지 관점 정리**를 기준으로 작성되었습니다.

---

## What I Focus On

### 🔍 APT Analysis
- Lazarus, Kimsuky, Andariel 등 실제 위협 그룹 분석
- MITRE ATT&CK 기반 TTP 구조화
- 단일 공격이 아닌 **캠페인 단위의 침해 흐름 분석**

### 🧪 BAS (Breach & Attack Simulation)
- APT 및 취약점 기반 공격 시나리오 시뮬레이션
- 방어 관점에서 재현 가능한 테스트 시나리오 설계
- 점검 자동화 및 재현성 확보에 중점

### 🛠 Vulnerability Research
- 공개 취약점 및 1-day 분석
- PoC 공유만이 아닌 **Root Cause / Attack Flow / Simulation / Mitigation / Detection** 중심 문서화
- 취약점을 실제 보안 점검 자산으로 전환하는 과정에 초점

---

## Repository Structure

```text
portfolio-root
├─ APT-Analysis        # APT 그룹별 분석 및 캠페인 정리
├─ BAS-Simulation      # 공격 시나리오 기반 시뮬레이션
├─ CVE-Research        # 취약점 분석 및 방어 관점 문서
├─ Tools               # 분석/자동화를 위한 보조 도구
└─ docs                # 포트폴리오 정책 및 공통 문서