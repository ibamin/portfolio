# Reversing Tools - GDB / WinDbg / Ghidra
## 구조 다이어그램

```mermaid
flowchart LR
    Goal["분석 목표"] --> Tool["도구 선택"]
    Tool --> Setup["환경 구성"]
    Setup --> Workflow["작업 흐름"]
    Workflow --> Output["결과 정리"]
```


Notion의 `리버싱 도구 > Smmary` 내용을 기반으로 정리한 동적/정적 분석 도구 치트시트입니다.

---

## GDB

### 기본 흐름
- `gdb ./sample`: 바이너리 로드
- `start`: `main` 진입 직전까지 실행
- `run`: 처음부터 실행
- `gdb -p <PID>`: 실행 중인 프로세스에 attach
- `quit`: 종료

### 핵심 명령
```text
run / r              : 프로그램 시작
continue / c         : 다음 BP/예외까지 계속
next / n             : 함수 호출은 건너뛰고 한 줄 실행
step / s             : 함수 안으로 진입
finish               : 현재 함수 리턴까지 실행
break main           : 함수 진입점 브레이크
break *0x401000      : 주소 기준 브레이크
info break           : 브레이크포인트 목록
info registers       : 레지스터 덤프
x/20xw $rsp          : 스택 메모리 확인
x/10i $rip           : 현재 명령어 주변 디스어셈블
backtrace / bt       : 콜스택
dump memory out.bin 0x605000 0x606000
```

### 분석 포인트
- 크래시 발생 시 `bt`, `info registers`, `x/40x $rsp`로 오염 위치를 확인합니다.
- `break open`, `break connect`, `break execve`처럼 시스템 호출 또는 라이브러리 호출 기준으로 행위를 관찰합니다.
- 복호화 완료 구간은 `dump memory`로 저장해 정적 분석에 재사용합니다.

---

## WinDbg

### 기본 흐름
- WinDbg Preview 또는 Windows SDK의 Debugging Tools for Windows를 설치합니다.
- 최초 분석 전 `.symfix`와 `.reload`로 Microsoft 심볼 서버를 설정합니다.
- 실행 파일을 열거나 프로세스에 attach한 뒤 `g`로 진행합니다.

### 핵심 명령
```text
.symfix; .reload
g / t / p / gu       : 계속 / step into / step over / 함수 리턴까지
bp KERNEL32!CreateFileW
bu KERNEL32!CreateProcessW
bl / bd / be / bc    : BP 목록 / 비활성 / 활성 / 삭제
k / kb / kp / kv     : 콜스택
r / r eax=0          : 레지스터 보기/수정
db / dd / dq / da / du: 메모리 보기
lm                   : 모듈 목록
x user32!*Box*       : 심볼 패턴 검색
!analyze -v          : 예외/크래시 자동 분석
!peb                 : PEB 확인
.logopen out.txt
.logclose
```

### 분석 포인트
- `CreateProcessW`, `VirtualAlloc`, `WriteProcessMemory`, `CreateRemoteThread`에 브레이크를 걸어 인젝션 흐름을 확인합니다.
- x64 인자는 RCX/RDX/R8/R9, x86 인자는 스택에서 확인합니다.
- 크래시 덤프는 `.dump /ma`로 저장한 뒤 `!analyze -v`, `kb`, `ub`, `u` 순서로 맥락을 확인합니다.

---

## Ghidra

### 기본 흐름
- 프로젝트 생성 후 바이너리를 Import하고 기본 분석을 실행합니다.
- PE 분석 시 외부 파라미터 전파 옵션을 켜면 API 인자 추적이 쉬워집니다.
- `Listing`, `Decompiler`, `Symbol Tree`, `Function Graph`를 함께 사용합니다.

### 분석 포인트
- Imports에서 `CryptUnprotectData`, `WinHttpSendRequest`, `RegSetValueExW` 같은 API를 먼저 확인합니다.
- Strings 검색으로 URL, 레지스트리 경로, 파일 경로, 명령 조각을 IOC 후보로 분류합니다.
- 의미 있는 함수명으로 rename하고 decompiler 주석을 남겨 가설과 근거를 연결합니다.
- 패킹 징후가 있으면 동적 분석으로 언패킹 후 메모리 덤프를 다시 로드합니다.

### Headless 예시
```bash
analyzeHeadless ./ProjDir MyProj \
  -import ./samples/mal.exe \
  -postScript DumpStrings.py \
  -deleteProject
```

---

## 안전한 실습 기준
- VM 스냅샷, 네트워크 격리, 공유 폴더 최소화를 기본값으로 둡니다.
- 관리자 권한은 필요한 순간에만 사용하고, 분석 산출물은 해시와 출처를 함께 기록합니다.
- 악성코드 실행, 유포, 외부 대상 테스트는 금지하고 학습/방어 목적의 격리 환경에서만 검증합니다.
