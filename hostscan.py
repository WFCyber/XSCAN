import argparse
import scapy.all as scapy

def scan_port(target, port):
    # 创建IP和TCP包
    ip_packet = scapy.IP(dst=target)
    tcp_packet = scapy.TCP(dport=port)

    # 合并IP和TCP包
    packet = ip_packet / tcp_packet

    # 发送并等待响应
    response = scapy.sr1(packet, timeout=1, verbose=False)

    # 判断响应是否为空，以及响应中是否包含TCP flags
    if response is not None and response.haslayer(scapy.TCP):
        if response.getlayer(scapy.TCP).flags == 0x12:  # 0x12表示SYN/ACK标志
            return True
        elif response.getlayer(scapy.TCP).flags == 0x14:  # 0x14表示RST标志
            return False
    return None

def scan_ports(target, ports):
    open_ports = []
    for port in ports:
        result = scan_port(target, port)
        if result is not None:
            if result:
                open_ports.append(port)
    return open_ports

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner using Scapy")
    parser.add_argument("target", help="Target host or IP address")
    parser.add_argument("-p", "--ports", type=str, help="Ports to scan (e.g., 80,443,8080)")
    args = parser.parse_args()

    target = args.target
    ports = args.ports.split(",") if args.ports else range(1, 1025)  # 默认扫描常见的端口范围

    open_ports = scan_ports(target, ports)

    if open_ports:
        print(f"Open ports on {target}: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
