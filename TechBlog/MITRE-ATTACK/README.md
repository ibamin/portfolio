# MITRE ATT&CK 기술 노트

MITRE ATT&CK 전술과 기법을 기준으로 공격 동작 방식, 관찰 포인트, 탐지/대응 방안을 정리합니다.  
각 글은 공격 실행 매뉴얼이 아니라 BAS 시나리오화와 탐지 엔지니어링을 위한 방어 관점의 기술 노트입니다.

---

## Initial Access
- [Malware Office - VBA 매크로 기반 초기 침투](Initial-Access/Malware-Office.md)
- [Word XML Link Tampering](Initial-Access/Word-XML-Link-Tampering.md)
- [T1078 - Valid Accounts](Initial-Access/T1078-Valid-Accounts.md)
- [T1133 - External Remote Services](Initial-Access/T1133-External-Remote-Services.md)
- [T1190 - Exploit Public-Facing Application](Initial-Access/T1190-Exploit-Public-Facing-Application.md)
- [T1566.001 - Spearphishing Attachment](Initial-Access/T1566.001-Spearphishing-Attachment.md)
- [T1566.002 - Spearphishing Link](Initial-Access/T1566.002-Spearphishing-Link.md)

## Execution
- [T1047 - Windows Management Instrumentation](Execution/T1047-Windows-Management-Instrumentation.md)
- [T1053.005 - Scheduled Task](Execution/T1053.005-Scheduled-Task.md)
- [T1059.001 - PowerShell](Execution/T1059.001-PowerShell.md)
- [T1059.003 - Windows Command Shell](Execution/T1059.003-Windows-Command-Shell.md)
- [T1059.004 - Unix Shell](Execution/T1059.004-Unix-Shell.md)

## Persistence
- [T1136.001 - Local Account Creation](Persistence/T1136.001-Local-Account-Creation.md)
- [T1543.003 - Windows Service](Persistence/T1543.003-Windows-Service.md)
- [T1546.003 - WMI Event Subscription](Persistence/T1546.003-WMI-Event-Subscription.md)
- [T1547.001 - Registry Run Keys / Startup Folder](Persistence/T1547.001-Registry-Run-Keys-Startup-Folder.md)
- [T1574.002 - DLL Side-Loading](Persistence/T1574.002-DLL-Side-Loading.md)

## Privilege Escalation
- [T1055 - Process Injection](Defense-Evasion/T1055-Process-Injection.md)
- [T1068 - Exploitation for Privilege Escalation](Privilege-Escalation/T1068-Exploitation-for-Privilege-Escalation.md)
- [T1134 - Access Token Manipulation](Privilege-Escalation/T1134-Access-Token-Manipulation.md)
- [T1548.002 - Bypass UAC](Privilege-Escalation/T1548.002-Bypass-UAC.md)
- [T1611 - Escape to Host](Privilege-Escalation/T1611-Escape-to-Host.md)

## Defense Evasion
- [DKOM - Direct Kernel Object Manipulation](Defense-Evasion/DKOM.md)
- [T1027 - Obfuscated Files or Information](Defense-Evasion/T1027-Obfuscated-Files-or-Information.md)
- [T1055 - Process Injection](Defense-Evasion/T1055-Process-Injection.md)
- [T1070.001 - Clear Windows Event Logs](Defense-Evasion/T1070.001-Clear-Windows-Event-Logs.md)
- [T1218.011 - Rundll32](Defense-Evasion/T1218.011-Rundll32.md)
- [T1562.001 - Disable or Modify Tools](Defense-Evasion/T1562.001-Disable-or-Modify-Tools.md)

## Credential Access
- [T1003.001 - LSASS Memory Dump](Credential-Access/T1003.001-LSASS-Memory-Dump.md)
- [T1110.003 - Password Spraying](Credential-Access/T1110.003-Password-Spraying.md)
- [T1552.001 - Credentials in Files](Credential-Access/T1552.001-Credentials-in-Files.md)
- [T1555.003 - Credentials from Web Browsers](Credential-Access/T1555.003-Credentials-from-Web-Browsers.md)
- [T1558.003 - Kerberoasting](Credential-Access/T1558.003-Kerberoasting.md)
- [T1558.004 - AS-REP Roasting](Credential-Access/T1558.004-AS-REP-Roasting.md)

## Discovery
- [T1018 - Remote System Discovery](Discovery/T1018-Remote-System-Discovery.md)
- [T1046 - Network Service Discovery](Discovery/T1046-Network-Service-Discovery.md)
- [T1057 - Process Discovery](Discovery/T1057-Process-Discovery.md)
- [T1082 - System Information Discovery](Discovery/T1082-System-Information-Discovery.md)
- [T1087.002 - Domain Account Discovery](Discovery/T1087.002-Domain-Account-Discovery.md)
- [T1135 - Network Share Discovery](Discovery/T1135-Network-Share-Discovery.md)

## Lateral Movement
- [T1021.001 - Remote Desktop Protocol](Lateral-Movement/T1021.001-Remote-Desktop-Protocol.md)
- [T1021.002 - SMB / Windows Admin Shares](Lateral-Movement/T1021.002-SMB-Admin-Shares.md)
- [T1534 - Internal Spearphishing](Lateral-Movement/T1534-Internal-Spearphishing.md)
- [T1550.002 - Pass the Hash](Lateral-Movement/T1550.002-Pass-the-Hash.md)

## Collection
- [T1005 - Data from Local System](Collection/T1005-Data-from-Local-System.md)
- [T1056.001 - Keylogging](Collection/T1056.001-Keylogging.md)
- [T1113 - Screen Capture](Collection/T1113-Screen-Capture.md)
- [T1114.001 - Local Email Collection](Collection/T1114.001-Local-Email-Collection.md)
- [T1560.001 - Archive via Utility](Collection/T1560.001-Archive-via-Utility.md)

## Command and Control
- [DCOM](Command-and-Control/DCOM.md)
- [PSEXEC](Command-and-Control/PSEXEC.md)
- [SC](Command-and-Control/SC.md)
- [Scheduler](Command-and-Control/Scheduler.md)
- [T1071.001 - Web Protocols](Command-and-Control/T1071.001-Web-Protocols.md)
- [T1090.003 - Multi-hop Proxy](Command-and-Control/T1090.003-Multi-hop-Proxy.md)
- [T1105 - Ingress Tool Transfer](Command-and-Control/T1105-Ingress-Tool-Transfer.md)
- [T1132.001 - Standard Encoding](Command-and-Control/T1132.001-Standard-Encoding.md)
- [T1572 - Protocol Tunneling](Command-and-Control/T1572-Protocol-Tunneling.md)
- [WINRM](Command-and-Control/WINRM.md)
- [WMIC](Command-and-Control/WMIC.md)

## Exfiltration
- [T1020 - Automated Exfiltration](Exfiltration/T1020-Automated-Exfiltration.md)
- [T1030 - Data Transfer Size Limits](Exfiltration/T1030-Data-Transfer-Size-Limits.md)
- [T1041 - Exfiltration Over C2 Channel](Exfiltration/T1041-Exfiltration-Over-C2-Channel.md)
- [T1048.003 - Exfiltration Over Unencrypted Protocol](Exfiltration/T1048.003-Exfiltration-Over-Unencrypted-Protocol.md)
- [T1567.002 - Exfiltration to Cloud Storage](Exfiltration/T1567.002-Exfiltration-to-Cloud-Storage.md)

## Impact
- [T1486 - Data Encrypted for Impact](Impact/T1486-Data-Encrypted-for-Impact.md)
- [T1489 - Service Stop](Impact/T1489-Service-Stop.md)
- [T1490 - Inhibit System Recovery](Impact/T1490-Inhibit-System-Recovery.md)
- [T1498 - Network Denial of Service](Impact/T1498-Network-Denial-of-Service.md)
- [T1529 - System Shutdown / Reboot](Impact/T1529-System-Shutdown-Reboot.md)

## Defense
- [Canary File - 침입 탐지용 미끼 파일](Defense/Canary-File.md)
