# WiFi-password-Stealer
WIP - A script to steal WiFi passwords


NOTE: This project is a work in progress. I keep it available to the public so employers can see which technologies I am investigating. While the code may not be complete for a while please keep checking in for when it is done!

-----------------------------------------------------------------------------------------

The aim of the script is to acquire the password of secured WAPs. It will be executed with a simple command:
'stealpassword <Target network's SSID>'.

The script works in two parts. The first is de-authenticating clients from a WAP and the second is by producing my own beacon frames with the same SSID.

To begin, the wireless adapter of the attacker will be put into monitor mode and will begin sniffing 802.11 frames. A beacon frame consists of three parts; a MAC header, a body and a FCS. By examining the type and subtype bits of the frame control field in the MAC header you can determine what traffic is beacon frames. In a beacon frame the type will be set to 0x01 to indicate management frame and the subtype will be 0xC to indicate beacon. A for loop is used to check for these conditions. If traffic is beacon frame traffic it will be investigated further. The SSID of the AP is found in the body of a beacon frame. If the SSID given in the argument of the command matches the SSID in a beacon frame, the source MAC address of that beacon frame will be assigned to a variable.

802.11 frames are again filtered but this time only those coming from the MAC address of the AP. The destination MAC addresses of these frames are appended to a list of MAC addresses to be de-authenticated. A function loops through this list sending a de-authentication packet to the AP with the source MAC address as each of the addresses in the list.

Meanwhile, in another thread, beacon frames are being crafted with the same SSID. Since everyone connected to the AP is being de-authenticated the hope is that at least one will type the password into the spoofed AP. When a user types in the password of the real access point into the fake one, an authentication frame containing the password will be sent to my MAC address and printed in the terminal.
