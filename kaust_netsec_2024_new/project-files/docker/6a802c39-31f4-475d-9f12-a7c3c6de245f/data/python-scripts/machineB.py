import socket
import sys
import struct

SERV_IP = '192.168.2.21'
P1 = 4857
SHUT_RDWR = 2

# Check the number of input arguments
if (len(sys.argv) < 4):
    raise Exception("Not enough input arguments.\n Usage : ./B P2 IP3 P3")

p2 = int(sys.argv[1])
ip3 = sys.argv[2]
p3 = int(sys.argv[3])

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the server on port P1
server_address = (SERV_IP, P1)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

# Send the 3 parameters to the server
ip3_be = socket.inet_aton(ip3)
p2_be = struct.pack('>H',p2)
p3_be = struct.pack('>H', p3)
message =  p2_be + '#' + ip3_be + '#' + p3_be
msg_len = len(message)
total_sent = 0
# Retry to send the parameters until everything has been sent
while (total_sent < msg_len):
    sent = sock.send(message[total_sent:])
    if sent == 0:
        raise RuntimeError("socket connection broken")
    total_sent = total_sent + sent

# Wait for user's interrupt and send the interrupt signal to the server
raw_input("Press enter to terminate")
sock.send('k')
sock.shutdown(SHUT_RDWR)
sock.close()

