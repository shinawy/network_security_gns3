"""
Very simple TCP server
syntax used is for Python3
Main differences with Python 2.* are in the 
print() command for formatting args
socket.send() which requires a bytes-like object, not a str
"""

import socket

PORT=5449

#Only the first def of HOST will enable you to connect from a remote machine
# (eg from one of your DSL machines if you run the server on the Xubuntu machine)
# Try it out by connecting with netcat or telnet on DSL to your Xubuntu machine

HOST="192.168.2.21"
#HOST='localhost'
#HOST=socket.gethostname()

print ("About to launch server on IP address {ip:s}, port {p:d}".format(ip=HOST,p=PORT))
srv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
srv.bind((HOST,PORT))
srv.listen(0)
# what is the influence of the parameter in srv.listen()???
# set the parameter to 0
# Launch wireshark. Try to connect three clients and see what happens
# kill all clients and server
# Set the parameter to 1 and redo the experiment with four clients
# What do you see? 

print("Ready to accept a connection")
conn, addr =srv.accept()
client_ip=addr[0]
client_port=addr[1]

print ("Server has accepted a connection from ip {ip:s},port {p:d}".format(ip=client_ip,p=client_port))

# conn.sendall("\00".encode())
# print("Just sent an empty packet, I think")

while True:
        data=conn.recv(1024)
# play with the parameter of recv() to see how many times you will pass in this loop
        if not data:
# what exactly is this "if" testing for?
# Connect to the server with NC. Send empty line. What happens?
                break
        print("Just got this from the netw buffer: {}".format(data))
        conn.send(data.upper())
# Verify with wireshark if you send as many packets as you are invoking conn.send()
# data is already a bytes-like object, so encode() is not needed for Python3
        
	
conn.close()
srv.close()
