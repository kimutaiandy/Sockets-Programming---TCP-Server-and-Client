import nmap

scanner = nmap.PortScanner()

print("Welcom, this is a simple nmap automation tool")
print("<------------------------------------------------->")

ip_addr = input("Please enter the IP Address you want to scan: ")
print("The ip address you entered is:", ip_addr)
type(ip_addr)

resp = input("""\n Please enter the type of scan you want to run
                 1) SYN ACK Scan
                 2) UDP Scan
                 3) Comprehensive scan""")
print("Yuo have selected option:", resp)

if resp =='1':
    print("Nmap Version", scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sS')
    print("Ip Status", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version", scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sU')
    print("Ip Status", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap Version", scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sS -sV -sC -A -O')
    print("Ip Status", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
    print("Please enter a valid option")