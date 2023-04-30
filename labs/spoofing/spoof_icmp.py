"""
This script will be a simple spoofer of ICMP packets. 
The idea is to send a ICMP packet to a host with a spoofed source ip address.
"""
import scapy.all as scapy


def spoof_icmp():
    """
    This function will capture ICMP packets and then send them back to the source
    modifying the source ip address.

    :return: None
    """
    packet = scapy.IP()
    packet.src = "1.2.3.4"
    packet.dst = "192.168.39.136"
    scapy.send(packet / scapy.ICMP())


if __name__ == "__main__":
    spoof_icmp()
