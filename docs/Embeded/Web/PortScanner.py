import requests
import threading

base_url = "http://192.168.0."
open_ports = []

def scan_port(ip, port):
    url = f"{base_url}{ip}:{port}"
    try:
        req = requests.get(url, timeout=1)
        if req.status_code == 200:
            print(url)
            open_ports.append(url)
        else:
            print("fail :"+url)
    except requests.ConnectionError:
        pass

def main():
    threads = []

    for ip in range(201, 256):
        for port in range(65000):
            scan_port(ip,port)

    print("Open ports:")
    for port in open_ports:
        print(port)

if __name__ == "__main__":
    main()
