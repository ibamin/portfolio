# Rust Security
<p class="doc-hero">
  <img class="doc-hero-image" src="../../assets/images/pexels-programming-6424584.jpg" alt="Programming code on screen" />
  <span class="doc-hero-caption">Image: Nemuel Sereti / Pexels</span>
</p>
## 구조 다이어그램

```mermaid
flowchart LR
    Code["Rust 코드"] --> Ownership["소유권/수명"]
    Ownership --> Unsafe["unsafe/FFI 경계"]
    Unsafe --> Review["보안 검토"]
    Review --> Hardening["하드닝"]
```


Rust 기반 보안 도구, 탐지 엔진, 시스템 프로그래밍 학습 내용을 정리하는 공간입니다.

---

## 예정 주제

- Rust CLI 보안 분석 도구
- 파일 해시/문자열 기반 탐지 엔진
- YARA/IOC 연동 구조
- Windows/Linux 이벤트 수집기 설계
- unsafe Rust와 FFI 보안 고려사항

리버스 엔지니어링 트랙을 완료한 뒤 Rust 기반 보안제품 개발 트랙에서 본격적으로 확장합니다.
