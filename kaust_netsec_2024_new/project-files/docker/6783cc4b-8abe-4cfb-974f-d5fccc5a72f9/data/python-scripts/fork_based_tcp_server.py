"""
A simple TCP server 
that can listen to several clients thanks to os.fork()

syntax used is for Python3
"""
import socket
import os
import sys

PORT= int(sys.argv[1])
HOST="192.168.2.21"

srv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((HOST,PORT))
srv.listen(1)
end="not yet"

while len(end) != 0:
    conn, addr =srv.accept()    

    if os.fork()==0:  #child process
      print("child is connected with client from {}".format(addr))
    
      while True:
        data=conn.recv(1024)
        if not data: break
        conn.send(data.upper())
      print("child is done with client from {}".format(addr))
      break
      
    else:
      print("nothing to do for the parent")
      end=input("<CR> = stop ; any char = Continue")
  
conn.close()
srv.close()

  
