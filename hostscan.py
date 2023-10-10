import json
import datetime

import nmap


def nmap_portscan(host, ports):  # 端口扫描
    nm = nmap.PortScanner()
    nm.scan('120.55.12.41', '22-1000')
    for host in nm.all_hosts():
        print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
    print('Protocol : %s' % proto)
    lport = nm[host][proto].keys()
    sorted(lport)
    for port in lport:
        print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))


def nmap_cli(host, port, args):  # 自定义命令行操作nmap
    current_time = datetime.datetime.now()  # 获取当前时间
    filename = current_time.strftime(f"{host}_%Y-%m-%d-%H-%M-%S")
    nm = nmap.PortScanner()
    rs = nm.scan(host, port, args)
    rs_json = json.dumps(rs,indent=4,separators=(',', ':'))
    with open(f'./target/namp/{filename}.json','w') as f:  # 扫描结果按照json保存在文件
        json.dump(rs, f,indent=4,separators=(',', ':'))
    print(rs_json)
    print(f'文件保存在./target/namp/{filename}.json')


if __name__ == '__main__':
    nmap_cli('120.55.12.41','22-1000','-O')
