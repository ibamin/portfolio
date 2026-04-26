# GNS3 네트워크 시뮬레이션
<p class="doc-hero">
  <img class="doc-hero-image" src="../../assets/images/pexels-programming-6424584.jpg" alt="Programming code on screen" />
  <span class="doc-hero-caption">Image: Nemuel Sereti / Pexels</span>
</p>
## 구조 다이어그램

```mermaid
flowchart LR
    Goal["분석 목표"] --> Tool["도구 선택"]
    Tool --> Setup["환경 구성"]
    Setup --> Workflow["작업 흐름"]
    Workflow --> Output["결과 정리"]
```


Notion의 `Network > GNS3` 내용을 기반으로 정리한 네트워크 실습 환경 메모입니다.

---

## 설치
- 다운로드: [GNS3 Software](https://gns3.com/software/download)
- 로그인 후 설치 파일을 내려받고 Installer를 실행합니다.
- 설치 과정에서 GNS3 VM을 함께 설치하면 라우터/보안 장비 시뮬레이션 구성이 편합니다.

---

## 기본 사용법

### 1. 프로젝트 생성
- GNS3 실행 후 **File > New blank project**를 선택합니다.
- 프로젝트 이름을 입력하고 작업 공간을 생성합니다.

### 2. 디바이스 추가
- 왼쪽 패널에서 라우터, 스위치, PC, 서버, 방화벽 등 필요한 디바이스를 작업 공간으로 드래그합니다.
- 장비별 템플릿과 이미지가 필요한 경우 사전에 등록합니다.

### 3. 디바이스 연결
- 케이블 아이콘을 선택하고 연결할 장비와 인터페이스를 지정합니다.
- Ethernet, Serial, Console 등 실습 목적에 맞는 연결 타입을 선택합니다.

### 4. 기본 라우터 설정 예시
```bash
enable
configure terminal
hostname Router1
interface GigabitEthernet0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
exit
```

### 5. 시뮬레이션 실행
- 상단 Start 버튼으로 장비를 실행합니다.
- `ping`, `traceroute`, Wireshark 캡처로 연결성과 패킷 흐름을 확인합니다.

---

## 운영 팁
- 스냅샷으로 특정 네트워크 상태를 보존합니다.
- 작업 공간에 Note와 라벨을 추가해 장비 역할, IP, 라우팅 의도를 기록합니다.
- 자주 쓰는 토폴로지는 템플릿으로 저장해 반복 실습 시간을 줄입니다.
- 공격/방어 시나리오 실습은 외부망과 분리된 랩 환경에서만 수행합니다.
