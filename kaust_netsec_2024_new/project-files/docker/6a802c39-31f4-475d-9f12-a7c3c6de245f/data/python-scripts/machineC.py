import socket
import sys
import struct

SERV_IP = '192.168.2.21'

print len(sys.argv)
# Check the number of input parameters
if (len(sys.argv) < 4 ):
    raise Exception("Not enough input arguments.\n Usage : ./C port M N")


p2 = int(sys.argv[1])
m, n = map(int, sys.argv[2:4])

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the server
server_address = (SERV_IP, p2)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

# Send m and n to server in 16 bits little endian
print >>sys.stderr, 'Sending integers...'
message = struct.pack('<hh', m, n)
msg_len = len(message)
total_sent = 0
while (total_sent < msg_len):
    sent = sock.send(message[total_sent:])
    if sent == 0:
        raise RuntimeError("socket connection broken")
    total_sent = total_sent + sent
print >>sys.stderr, 'Done'
