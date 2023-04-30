"""
Based on previous code, we do a general sniffer and use it with different filters.
"""
import scapy.all as scapy


def show_packages(
    filter: str,
    prn: callable = lambda x: x.show(),
    count: int = 1,
    iface: str = scapy.conf.iface,
):
    """
    This function will capture ICMP packets in the network

    :param filter: filter to apply to sniff
    :param prn: function to execute for each packet
    :param count: number of packets to capture
    :param iface: interface to sniff

    :return: ICMP packets
    """
    icmp_packages = scapy.sniff(prn=prn, count=count, filter=filter, iface=iface)
    return icmp_packages


if __name__ == "__main__":
    dest_ip = "192.168.39.136"
    show_packages(filter=f"tcp port 23 and src net {dest_ip}", count=2)
