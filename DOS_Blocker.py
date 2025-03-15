print("#########################################")
print("#          MINIMAL DOS BLOCKER          #")
print("#########################################\n")

import os
import sys
import time
from collections import defaultdict
from scapy.all import sniff, IP

#Packet Rate Limit
THRESHOLD = 50
print(f"Threshold Limit = {THRESHOLD}")                          

#Tracking network activity
packet_count = defaultdict(int)
start_time = [time.time()]
blocked_ips = set()

def packet_callback(packet):
    source_ip = packet[IP].src                                  #Extracts source IP
    packet_count[source_ip] += 1                                #Increments packet count for the IP

    current_time = time.time()                                  #Get current time
    time_interval = current_time - start_time[0]  

    if time_interval >= 1:                                      #Check if 1 second has passed
        for ip, count in packet_count.items():
            packet_rate = count / time_interval  

            if packet_rate > THRESHOLD and ip not in blocked_ips:
                print(f"Blocking IP: {ip}, Packets: {packet_rate}")
                os.system(f"iptables -A INPUT -s {ip} -j DROP")
                blocked_ips.add(ip)

        packet_count.clear()                                      #Reset packet count
        start_time[0] = current_time                              #Update start time

                                                                    #Ensure script is run as root
if os.geteuid() != 0:
    print("RUN AS ROOT")
    sys.exit(1)
    
print("Monitoring Traffic Now...")
sniff(filter="ip", prn=packet_callback)
