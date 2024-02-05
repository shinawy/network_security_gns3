"""
Very simple  TCP server with non blocking socket
syntax used is for Python3
"""
import socket
import errno
import time
import sys

PORT= int(sys.argv[1])
HOST="192.168.2.21"

srv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
srv.bind((HOST,PORT))
srv.listen(2)

conn, addr =srv.accept()

conn.setblocking(False)

while True:
  try:
                data=conn.recv(1024)
                if not data: break
                else:
                 print("---")
                 conn.sendall(data.upper())
  except(socket.error) as e:
                  if e.args[0] == errno.EWOULDBLOCK:
                                  print("*",end="")
                                  time.sleep(1)
                                  print("#",end="")
print("===")
conn.close()
srv.close()
