import scapy.all as scapy
import argparse

# 1) Arp Request
# 2) Broadcast
# 3) Responde

def user_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--ip-address",dest="ip_address",help="Enter IP address")
    args = parser.parse_args()
    return args.ip_address

def scan_net(ip):
    arp_request_packet = scapy.ARP(pdst=ip)

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combined_packet = broadcast_packet/arp_request_packet

    answered,unanswered=scapy.srp(combined_packet,timeout=1)

    answered.summary()


scan_net(user_input())