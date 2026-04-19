# DKOM — Direct Kernel Object Manipulation

## 개요

DKOM이란 Direct Kernel Object Manipulation의 약자로 커널 오브젝트를 직접 수정하는 행위를 의미하며, 이를 통해 프로세스 은닉, 디바이스 드라이버 은닉, 스레드 권한 상승, 프로세스 권한 상승, 포렌식 회피 등이 가능합니다.

---

## 사전 지식

### PEB (Process Environment Block)

Process Environment Block은 프로세스 정보를 담고 있는 구조체로, TEB(Thread Environment Block)를 통해 참조됩니다.

```c
// Thread Environment Block Structure
typedef struct _TEB {
  PVOID Reserved1[12];
  PPEB  ProcessEnvironmentBlock;
  PVOID Reserved2[399];
  BYTE  Reserved3[1952];
  PVOID TlsSlots[64];
  BYTE  Reserved4[8];
  PVOID Reserved5[26];
  PVOID ReservedForOle;
  PVOID Reserved6[4];
  PVOID TlsExpansionSlots;
} TEB, *PTEB;

// Process Environment Block
typedef struct _PEB {
  BYTE                          Reserved1[2];
  BYTE                          BeingDebugged;
  BYTE                          Reserved2[1];
  PVOID                         Reserved3[2];
  PPEB_LDR_DATA                 Ldr;
  PRTL_USER_PROCESS_PARAMETERS  ProcessParameters;
  PVOID                         Reserved4[3];
  PVOID                         AtlThunkSListPtr;
  PVOID                         Reserved5;
  ULONG                         Reserved6;
  PVOID                         Reserved7;
  ULONG                         Reserved8;
  ULONG                         AtlThunkSListPtr32;
  PVOID                         Reserved9[45];
  BYTE                          Reserved10[96];
  PPS_POST_PROCESS_INIT_ROUTINE PostProcessInitRoutine;
  BYTE                          Reserved11[128];
  PVOID                         Reserved12[1];
  ULONG                         SessionId;
} PEB, *PPEB;
```

**프로세스 트리 구조:**
```
Process
├─ PEB 1개
├─ Thread 1
│  └─ TEB 1개 ──> PEB를 가리킴
├─ Thread 2
│  └─ TEB 1개 ──> 같은 PEB를 가리킴
└─ Thread 3
   └─ TEB 1개 ──> 같은 PEB를 가리킴
```

### PEB 접근 실습 (Rust)

```toml
# Cargo.toml
[dependencies]
windows_sys = { version = "0.61.2", features = ["Win32_System_Threading"] }
```

```rust
// main.rs
use windows_sys::Win32::System::Threading::{PEB, TEB};

#[cfg(target_arch = "x86_64")]
unsafe fn current_teb() -> *mut TEB {
    let teb: *mut TEB;
    core::arch::asm!(
        "mov {}, gs:[0x30]",
        out(reg) teb,
        options(nostack, preserves_flags)
    );
    teb
}

#[cfg(target_arch = "x86")]
unsafe fn current_teb() -> *mut TEB {
    let teb: *mut TEB;
    core::arch::asm!(
        "mov {}, fs:[0x18]",
        out(reg) teb,
        options(nostack, preserves_flags)
    );
    teb
}

fn main() {
    unsafe {
        let teb = current_teb();
        if teb.is_null() {
            eprintln!("TEB is null");
            return;
        }

        let peb: *mut PEB = (*teb).ProcessEnvironmentBlock;
        if peb.is_null() {
            eprintln!("PEB is null");
            return;
        }

        println!("[+] TEB = {:p}", teb);
        println!("[+] PEB = {:p}", peb);
        println!("[+] BeingDebugged = {}", (*peb).BeingDebugged);
        println!("[+] Ldr = {:p}", (*peb).Ldr);
        println!("[+] ProcessParameters = {:p}", (*peb).ProcessParameters);
        println!("[+] SessionId = {}", (*peb).SessionId);
    }
}
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: Windows Defender Realtime Protection Disabled
status: stable
logsource:
  product: windows
  service: windefend
detection:
  selection:
    EventID: 5001
  condition: selection
level: critical
tags:
  - attack.defense_evasion
  - attack.t1562.001
```

---

## 대응 방안

1. Kernel Patch Protection (KPP/PatchGuard) 활성화
2. 드라이버 서명 강제 (Driver Signature Enforcement)
3. 커널 오브젝트 무결성 모니터링

---

## 참고자료
- [DKOM 기법 설명](https://nameng.tistory.com/93)
- [PEB 구조체](https://kblab.tistory.com/301)
- [Processes and Threads - Win32](https://learn.microsoft.com/en-us/windows/win32/procthread/processes-and-threads)
- [TEB - Win32 API](https://learn.microsoft.com/ko-kr/windows/win32/api/winternl/ns-winternl-teb)
