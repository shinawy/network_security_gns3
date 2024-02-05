import socket
import sys
import struct

# Local host
HOST = ''

# Check the number of input arguments
if (len(sys.argv) != 2):
    raise Exception("Not enough input arguments.\n Usage : ./D P3")

p3 = int(sys.argv[1])

# Creta TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, p3))

# Start listening on port P3 and accept connection
s.listen(1)

while (1) :
    (conn,addr) = s.accept()
    print >>sys.stderr, 'Connected with', addr
    
    # Read continuously data received from A
    while (1) :
        # The output of machine A is a 32 bits signed integer number
        data = conn.recv(8)
        if (len(data) != 8):
            break
        (sum_,product) = struct.unpack('<ii',data)
        print >>sys.stderr, 'Received : %s and %s' % (sum_,product)
