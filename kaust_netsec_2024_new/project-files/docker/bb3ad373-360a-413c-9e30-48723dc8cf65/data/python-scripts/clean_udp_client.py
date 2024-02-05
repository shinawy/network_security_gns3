"""
Very Simple UDP client.
syntax used is for Python 3
"""
import socket

PORT=4444
HOST="192.168.2.21"

cli=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
cli.connect((HOST,PORT))

while True:
	cmd=input("Input:  ")	
	if len(cmd)==0: break
	cli.send(cmd.encode())
	ans=cli.recv(1024)
	print ("Output: {}".format(ans.decode()))

#let the server know we are gone
cli.send("".encode())
cli.close()
