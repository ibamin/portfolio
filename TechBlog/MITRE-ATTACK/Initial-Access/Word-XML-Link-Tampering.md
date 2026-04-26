# Word XML Link Tampering

## 개요

**Initial Access / Custom**  
Word 문서의 OpenXML 관계 파일을 변조해 외부 템플릿이나 문서 리소스를 공격자 제어 위치로 참조하게 만드는 초기 침투 기법입니다.

---

## 동작 방식

- `word/_rels/settings.xml.rels` 같은 관계 파일에서 외부 Target URL을 조작합니다.
- 피해자가 문서를 열면 Word가 외부 리소스를 가져오며 악성 매크로 문서 또는 추가 페이로드로 이어질 수 있습니다.
- 정상 템플릿 문서처럼 보이기 때문에 첨부파일 평판과 문서 내부 관계 검사가 중요합니다.

---

## 탐지 포인트

- Office 문서 내부의 `.rels` 파일에서 외부 HTTP/HTTPS Target 참조를 검사합니다.
- WINWORD.EXE가 문서 열람 직후 비정상 외부 도메인으로 연결하는지 확인합니다.
- Office 프로세스의 자식 프로세스 생성과 문서 다운로드 이벤트를 함께 봅니다.

---

## 대응 방안

1. 인터넷에서 받은 Office 문서의 매크로와 외부 템플릿 로딩을 제한합니다.
2. 메일 게이트웨이에서 Office OpenXML 내부 관계 파일의 외부 URL을 검사합니다.
3. 사용자 환경에서 Protected View, ASR 규칙, 신뢰할 수 있는 위치 정책을 적용합니다.

---

## 참고자료

- [MITRE ATT&CK Custom](https://attack.mitre.org/techniques/Custom/)
- OpenXML 관계 파일 구조와 외부 템플릿 참조 동작은 Microsoft Office 문서 보안 점검 항목에 포함해 관리합니다.
