"""
Simple concurrent TCP server using threads
"""
import socket
import os
import threading

PORT=4444
HOST="192.168.2.21"

class ClientSocket(threading.Thread):
# yes, ClientSocket is a misleading name since it is running on the server but ..
	
	def __init__(self,sock,addrinfo):
		threading.Thread.__init__(self) #don't forget!
		
		self.conn=sock
		self.addr=addrinfo
		self.daemon=True #no need to join
	
	def run(self):
		print("Server has established connection with client from {}".format(self.addr))
		while True:
			data=self.conn.recv(1024)
			if not data: break
			self.conn.send(data.upper())
		self.conn.close()
		print("Server disconnected with client at {}".format(self.addr))
		

srv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
srv.bind((HOST,PORT))
srv.listen(1)

while True:
	conn,addr=srv.accept()
	#create the thread and forget about it
	ClientSocket(conn,addr).start()
	
