"""
Very simple UDP server.
Syntax used is for Python 3
"""
import socket

PORT=4444
HOST="192.168.2.21"

srv=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
srv.bind((HOST,PORT))

while True:
	data,addr=srv.recvfrom(1024)
	if not data: break
	srv.sendto(data.upper(),addr)
	
srv.close()
