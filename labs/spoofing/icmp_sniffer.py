"""
This second sniffer will capture ICMP packets in the network
"""
import scapy.all as scapy


def get_icmp_packages(
    prn: callable = lambda x: x.show(),
    count: int = 1,
    filter: str = "icmp",
    iface: str = scapy.conf.iface,
):
    """
    This function will capture ICMP packets in the network

    :param prn: function to execute for each packet
    :param count: number of packets to capture
    :param filter: filter to apply to sniff
    :param iface: interface to sniff

    :return: ICMP packets
    """
    icmp_packages = scapy.sniff(prn=prn, count=count, filter=filter, iface=iface)
    return icmp_packages


if __name__ == "__main__":
    get_icmp_packages(count=2)
