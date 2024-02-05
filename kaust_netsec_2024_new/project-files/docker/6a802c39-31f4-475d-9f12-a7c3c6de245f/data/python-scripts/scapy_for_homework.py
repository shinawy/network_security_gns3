import scapy.all as scapy
import socket
import struct
import sys

scapy.conf.L3socket
scapy.conf.L3socket=scapy.L3RawSocket


# args to be sent to machineA
p2=2222
ip3="127.0.0.1"
p3=3333
ip3_be = socket.inet_aton(ip3)
p2_be = struct.pack('>H',p2)
p3_be = struct.pack('>H', p3)
first_half=p2_be + '#'
second_half=ip3_be + '#' + p3_be
full_message =  first_half + second_half

# connection establishment

sport = int(sys.argv[1])
src=dest="127.0.0.1"
dport=4857
ip=scapy.IP(src=src,dst=dest)
SYN=scapy.TCP(sport=sport,dport=dport,flags='S',seq=1000)
SYNACK=scapy.sr1(ip/SYN)

ACK=scapy.TCP(sport=sport,dport=dport,flags='A',seq=SYNACK.ack,ack=SYNACK.seq+1)
scapy.send(ip/ACK/full_message)

# to be nice, you should send the FIN/ACK, ACK pkts now ...
