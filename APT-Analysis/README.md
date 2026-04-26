# APT-Analysis
<p class="doc-hero">
  <img class="doc-hero-image" src="../assets/images/pexels-cyber-binary-5473951.jpg" alt="Cybersecurity binary code projection" />
  <span class="doc-hero-caption">Image: cottonbro studio / Pexels</span>
</p>
## 구조 다이어그램

```mermaid
flowchart TD
    Intel["위협 인텔리전스"] --> Actor["APT-Analysis"]
    Actor --> TTP["TTP 분석"]
    TTP --> Scenario["공격 시나리오"]
    Scenario --> Detection["탐지 포인트"]
    Detection --> Response["대응/완화"]
```


APT 그룹별 자료를 모아둔 폴더입니다.

## Groups
- [Andariel](Andariel/README.md)
- [Kimsuky](Kimsuky/README.md)
- [Lazarus](Lazarus/README.md)
- [Lockbit](Lockbit/README.md)
- [OilRig](OilRig/README.md)
- [Qilin](Qilin/README.md)
- [SideWinder](SideWinder/README.md)

## Featured Scenarios
- [OilRig DB 백업 유출 시나리오](OilRig/Scenario-DB-Backup-Exfil.md)
- [Lazarus 도메인 정책 기반 인프라 장악 시나리오](Lazarus/Scenario-Domain-Policy-PMS.md)
- [SideWinder Template Injection to Stealer](SideWinder/Template-Injection-Stealer.md)
- [Qilin Ransomware Trend Analysis](Qilin/Ransomware-Trend-Analysis.md)
