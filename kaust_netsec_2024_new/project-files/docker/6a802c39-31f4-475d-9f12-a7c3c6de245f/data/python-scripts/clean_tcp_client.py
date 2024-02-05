"""
Very simple client
Syntax used is for Python 3
"""
import socket

PORT = 4445
HOST = "192.168.2.21"

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((HOST, PORT))

while True:
  cmd = input("Input: ")
  if len(cmd) == 0: break
  cli.sendall(cmd.encode())
  ans=cli.recv(1024)
  print ("Output: {up:s}".format(up=ans.decode()))
  
cli.close()
