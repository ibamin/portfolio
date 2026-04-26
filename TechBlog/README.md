# Tech Blog
<p class="doc-hero">
  <img class="doc-hero-image" src="../assets/images/pexels-cyber-binary-5473951.jpg" alt="Cybersecurity binary code projection" />
  <span class="doc-hero-caption">Image: cottonbro studio / Pexels</span>
</p>
## 구조 다이어그램

```mermaid
flowchart LR
    Topic["Tech Blog"] --> Concept["핵심 개념"]
    Concept --> Practice["실습/분석"]
    Practice --> Notes["정리"]
    Notes --> Reuse["재사용 가능한 기준"]
```


보안 연구 과정에서 정리한 기술 블로그입니다. 공격 기법을 단순히 나열하지 않고, 분석 근거와 방어 관점의 대응으로 연결하는 것을 목표로 합니다.

---

## Sections

### MITRE ATT&CK

MITRE ATT&CK 전술/기법을 기준으로 공격 동작 방식, 관찰 포인트, 탐지/대응 방안을 정리합니다.  
Notion의 `나만의 기술 블로그`에 있던 Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact 항목을 반영했습니다.

- [MITRE ATT&CK 기술 노트](MITRE-ATTACK/README.md)

### Reverse Engineering

Dreamhack, CTF, 교육용 바이너리 분석을 통해 정적 분석, 디컴파일러 검증, 조건 분기 추적, 런타임 검증 과정을 기록합니다.

- [Reverse Engineering 노트](Reversing/README.md)

대표 Writeup: [Dreamhack rev-basic-0 분석 노트](Reversing/Dreamhack-rev-basic-0.md)

### Toolbox Notes

Notion의 `도구 모음`에 있던 리버싱 도구와 네트워크 실습 환경 메모를 별도 섹션으로 분리했습니다.

- [Toolbox Notes](Toolbox/README.md)
- [Reversing Tools - GDB / WinDbg / Ghidra](Toolbox/Reversing-Tools.md)
- [GNS3 네트워크 시뮬레이션](Toolbox/GNS3.md)

### Malware Analysis Notes

악성코드 분석 보고서에서 다루기 전 단계의 기술 메모, 분석 패턴, 도구 사용법을 정리하는 공간입니다.

- [Malware Analysis 기술 노트](Malware-Analysis/README.md)

### Rust Security

Rust 기반 보안 도구, 탐지 엔진, 시스템 프로그래밍 학습 내용을 정리하는 공간입니다.

- [Rust Security 노트](Rust-Security/README.md)

---

## Featured

- [T1190 - Exploit Public-Facing Application](MITRE-ATTACK/Initial-Access/T1190-Exploit-Public-Facing-Application.md)
- [T1547.001 - Registry Run Keys / Startup Folder](MITRE-ATTACK/Persistence/T1547.001-Registry-Run-Keys-Startup-Folder.md)
- [T1562.001 - Disable or Modify Tools](MITRE-ATTACK/Defense-Evasion/T1562.001-Disable-or-Modify-Tools.md)
- [T1041 - Exfiltration Over C2 Channel](MITRE-ATTACK/Exfiltration/T1041-Exfiltration-Over-C2-Channel.md)
- [T1486 - Data Encrypted for Impact](MITRE-ATTACK/Impact/T1486-Data-Encrypted-for-Impact.md)
- [Reversing Tools - GDB / WinDbg / Ghidra](Toolbox/Reversing-Tools.md)
