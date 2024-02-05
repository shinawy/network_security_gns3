"""
A very simple program to demonstrate how to use scapy to complete
a TCP three way handshake.
Usage:
python simple_3way_scapy <src_ip> <dest_ip> <dest_port>

<src_ip> and <dest_ip> can either be an IP address or 
a FQDN or "localhost"

You only need the "magic" two first commands if you plan on using 
the loopback interface

Also, you will need to configure iptables properly to avoid 
generating a RST packet that would prevent you from completing the
three way handshake properly

iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP

"""


from scapy.all import *

# magic required if using the loopback interface
conf.L3socket
conf.L3socket=L3RawSocket


# VARIABLES
src = sys.argv[1]
dst = sys.argv[2]
sport = random.randint(1024,65535)
dport = int(sys.argv[3])

# SYN
ip=IP(src=src,dst=dst)
SYN=TCP(sport=sport,dport=dport,flags='S',seq=1000)
SYNACK=sr1(ip/SYN)

# ACK
ACK=TCP(sport=sport, dport=dport, flags='A', seq=SYNACK.ack, ack=SYNACK.seq + 1)
send(ip/ACK)
