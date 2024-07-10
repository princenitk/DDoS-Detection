from scapy.all import *

def launch_traffic(start,end):
    #dst_port=80
    for i in range(start,end+1):
        #src_ip=".".join(str(random.randint(1,255)) for _ in range(4))
        src_ip=f'10.0.0.{random.randint(1,20)}'
        
        dst_ip=f'10.0.0.{random.randint(1,18)}'
        
        if(src_ip == dst_ip):
            continue
        
        src_port=random.randint(1,5)
        dst_port=random.randint(1,5)
        protocol=random.choice(['TCP','UDP','ICMP'])
        
        if protocol=='TCP':
            packet=Ether(type=0x800) / IP(src=src_ip, dst=dst_ip) / TCP(sport=src_port, dport=dst_port)
        elif protocol=='UDP':
            packet=Ether(type=0x800) / IP(src=src_ip, dst=dst_ip) / UDP(sport=src_port, dport=dst_port)
        elif protocol=='ICMP':
            packet=Ether(type=0x800) / IP(src=src_ip, dst=dst_ip) / ICMP()


        #packet=Ether(type=0x800) / IP(src=src_ip, dst=dst_ip) / UDP(sport=2, dport=dst_port)

        print(repr(packet))

        sendp(packet,iface='h1-eth0', verbose=False)

if __name__=="__main__":
    import argparse

    parser=argparse.ArgumentParser(description='Launch UDP traffic simulation.')
    parser.add_argument('-s', '--start',type=int, help='Start index for destination IP addresses', required=True)
    parser.add_argument('-e', '--end', type=int, help='End index for destination IP addresses', required=True)

    args=parser.parse_args()
    launch_traffic(args.start,args.end)

'''
from scapy.all import *
import random
 
def generate_traffic(src, dst, sport, dport, count):
    for _ in range(count):
        ip = IP(src=src, dst=dst)
        udp = UDP(sport=sport, dport=dport)
        packet = ip/udp
        send(packet)
 
def launch_traffic():
    # Define the source and destination IP addresses
    src_ip = "10.0.0.2"  # Source IP (Host 2)
    dst_ips = ["10.0.0.76", "10.0.0.180", "10.0.0.17", "10.0.0.94", "10.0.0.167"]  # Destination IPs
 
    # Define the source and destination ports
    sport = random.randint(1024, 65535)  # Source port
    dport = 80  # Destination port (HTTP)
 
    # Define the number of packets to send
    count = 200
 
    # Generate and send the traffic
    for dst_ip in dst_ips:
        generate_traffic(src_ip, dst_ip, sport, dport, count)
 
if _name_ == "_main_":
    launch_traffic()
'''