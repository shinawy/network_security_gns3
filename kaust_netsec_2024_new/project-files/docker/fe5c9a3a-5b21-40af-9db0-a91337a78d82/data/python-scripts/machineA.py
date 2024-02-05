import socket
import struct
import sys
import os

# P1
PORT = 4857
# Empty host is lacalhost
HOST = ''
# NO_INTER means no interrupt received from B
NO_INTER = 'a'
# Normally defined in socket, but python can't always find socket.SHUT_RDWR
SHUT_RDWR = 2

###########################$

# Create socket for incoming connection
def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return sock

# Close a conncetion properly
def close_connection(conn):
    conn.shutdown(SHUT_RDWR)
    conn.close()


# Send data over a connection
# Retry until all the data has been sent or the connection is lost
def send_data(conn, msg):
    msg_len = len(msg)
    total_sent = 0
    # Keep sending remaining bytes until the full message is transmitted
    while (total_sent < msg_len):
        sent = conn.send(msg[total_sent:])
        if sent == 0:
            raise RuntimeError("Socket connection broken")
        total_sent = total_sent + sent


# connect_to_D handles the connection to machine D : 
# It tries 3 times with a 30 ms timeout
def connect_to_D(sock, ip3, p3):
    # Attempt to connect to D 3 times with a 30 ms timeout
    sock.settimeout(0.03)
    t = 3
    while (t != 0 and t != -1):
        try :
            sock.connect((ip3, p3))
            t = -1
        except :
            t = t - 1
            continue
    # t == 0 means connection failed
    return sock, t 


# handle_C operate the exchange between a machine C and D
def handle_C(conn_C, ip3, p3):
    # Set timeout to 10 ms 
    conn_C.settimeout(0.01)
    # Wait to receive 4 bytes. If not received within 10 ms, close connection and exit.
    try :
        integers = conn_C.recv(4)
    except socket.timeout:
        close_connection(conn_C)
        print >> sys.stderr, "No parameters received from C"
        os._exit(1)

    # Once we have the parameters, we close the connection to C
    close_connection(conn_C)
    
    # Check the length of the received data
    if (len(integers) != 4):
        print >> sys.stderr, "Not enough parameters from C, closing connection"
        close_connection(conn_C)
        os._exit(1)

    # Try to unpack the data according to the expected format
    try :
        (m,n) = struct.unpack('<hh', integers)
        print >>sys.stderr, "Parameters received from C : ", m, n
    except :
        print >> sys.stderr, "Parameter error (C): Wrong format"
        os._exit(1)
    if(m*n < 0):
	print >>sys.stderr, "bad values"
        os._exit(1)
    
    # Compute the 2 results to send to D
    sum_ = m+n
    product = m*n
    results = struct.pack('<ii', sum_, product)
    
    # Establish a connection to D
    # If it fails, exit
    sock_3 = create_socket()
    client_address = (ip3, p3)
    sock_3, t = connect_to_D(sock_3, ip3, p3)
    if (t == 0):
        print >>sys.stderr, "Connection to D failed"
        os._exit(1)

    # Send m+n and m*n to machine D in 16 bits little endian
    print >>sys.stderr, 'Sending integers : ', sum_, product
    send_data(sock_3, results) 
    print >>sys.stderr, 'Integers sent, closing connection with C'


    # Close connection to D and exit child process
    close_connection(sock_3)
    os._exit(0)


# Main funciton of the server
def server():
    print >>sys.stderr, "Server started"

    # Create a socket to misten on port P1
    sock_1 = create_socket()
    sock_1.bind((HOST, PORT))
    sock_1.listen(10)

    while(1):
        print >>sys.stderr, "## Waiting for a connection from a client B"
        
        # Accept connection on port P1
        (conn_B, addr) = sock_1.accept()
        
        print >>sys.stderr, "Connection received from B ", addr
        
        # Wait to receive parameters from machine B
        # If it fails, close connection and go to next iteration
        conn_B.settimeout(0.01)
        try :
            data = conn_B.recv(10)
        except socket.timeout :
            print >> sys.stderr, "No parameters received from B, closing connection"
            close_connection(conn_B)
            continue

        # Check the length of the received data
        if (len(data) != 10):
            print >> sys.stderr, "Not enough parameters from B, closing connection"
            close_connection(conn_B)
            continue

        # Try to unpack the data according to the expected format
        try :
            # 8 bits ports, 32 bits IP address
            p2 = struct.unpack('>H',data[:2])[0]
	    p3 = struct.unpack('>H',data[8:10])[0]
	    ip3 = socket.inet_ntoa(data[3:7])
            print >>sys.stderr, "Parameters received from B : ", p2, ip3, p3
        except :
            print >> sys.stderr, "Parameter error (B): wrong format "
            close_connection(conn_B)
            continue

        # Check if P2 and P3 are different from P1
        if (p2 == PORT or p3 == PORT):
            print >> sys.stderr, "P2 should be different from P3 "
            close_connection(conn_B)
            continue
	if(p2 > 65537 or p3 > 65537):
                 print >> sys.stderr, "bad ports "
                 close_connection(conn_B)
                 continue
	

	
		
 
       # Create a socket to listen on P2
        sock_2 = create_socket()
        sock_2.bind((HOST, p2))
        sock_2.listen(5)
        sock_2.settimeout(0.01)
        
        # inter equals 'k' if an interrupt is received from B
        inter = NO_INTER
        
        while (inter != 'k'):
            # Accept a new connection on port P2
            try :
                conn_C, addr_C = sock_2.accept()
                print >>sys.stderr, "# Connection received from C ", addr_C
                # Create a new thread to handle it
                p_id = os.fork()
                if (p_id == 0):
                    handle_C(conn_C, ip3, p3)
            except socket.timeout :
                pass

            # Check if B has sent an interrupt between 2 C-D exchanges
            try :
                inter = conn_B.recv(1)
            except socket.timeout :
                pass

        # When an interrupt is received from B, close connection to B
        print >>sys.stderr, "Received interrupt signal from B, closing connection"
        close_connection(sock_2)
        close_connection(conn_B)

###########################

# Launch the server
server()

