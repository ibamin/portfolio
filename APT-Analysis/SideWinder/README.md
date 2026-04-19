# SideWinder APT Group

## 개요

| 항목 | 내용 |
|------|------|
| **활동 시기** | 2012년 ~ 현재 |
| **표적 지역** | 파키스탄, 스리랑카, 중국, 네팔 (남아시아) |
| **표적 섹터** | 정부, 군사, 물류, 항만 |
| **공격 목적** | 장기적 정보 수집, 스파이 활동 |
| **주요 기법** | Template Injection, DLL Side-Loading, LOLBin 남용 |

---

## 분석 자료

| 문서 | 핵심 기법 | ATT&CK |
|------|-----------|--------|
| [Template Injection to Stealer](APT-Analysis/SideWinder/Template-Injection-Stealer.md) | Template Injection → HTA Downloader → DLL Side-Loading | T1221, T1574.002, T1053.005 |

---

## 주요 TTP

- **Initial Access**: Spearphishing + Template Injection (T1221)
- **Execution**: HTA Downloader via mshta.exe (T1204.002)
- **Persistence**: LOLBin(pcalua.exe) + Scheduled Task / Registry Run Key
- **Defense Evasion**: DLL Side-Loading (T1574.002)
- **Discovery**: 메모리 환경 파악 + 보안 제품 탐지 (T1082, T1518.001)
