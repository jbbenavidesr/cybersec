"""
The first sniffer is very simple and will simply print the ip address of the local machine.
"""
import scapy.all as scapy


def get_ip_address(iface: str = scapy.conf.iface):
    """
    This function will get the ip address of the local machine.

    :param iface: interface to get ip address from

    :return: ip address
    """
    ip_address = scapy.get_if_addr(iface)
    return ip_address


if __name__ == "__main__":
    print(get_ip_address())
