#! /usr/bin/env python

import optparse
import scapy.all as scapy

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-t","--target",dest="target", help="Target IP/IP range ")
    options=parser.parse_args()[0]
    return options

def scan(ip):
    arp_request =scapy.ARP(pdst=ip)
    broadcast =scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast =broadcast/arp_request
    answered_list =scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    print("IP\t\t\t\tMAC Address \n---------------------------------------------------")
    response_list=[]
    for element in answered_list:
        sub_entries={"ip":element[1].psrc,"mac":element[1].hwsrc}
        response_list.append(sub_entries)
    return response_list
options=get_arguments()
scan_results=scan(options.target)
print("IP\t\t\tMAC Address\n-----------------------------------------------------------------------------")
for entries in scan_results:
    print(entries["ip"]+"\t\t"+entries["mac"])

