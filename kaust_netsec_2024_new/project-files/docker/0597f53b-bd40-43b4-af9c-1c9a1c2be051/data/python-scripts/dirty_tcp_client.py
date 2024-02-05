"""
Very simple client
Syntax used is for Python 3
"""

import socket

PORT = 5449
HOST = "192.168.2.21"

# The next two choices for HOST are only valid if the server runs on the same
# machine as the client and has been launched to listen to the loopback address.
# HOST = 'localhost'
# HOST = socket.gethostname()

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("About to connect to  server on IP address {ip:s}, port {p:d}".format(ip=HOST,p=PORT))
cli.connect((HOST, PORT))
print("A successfull three way handshake has taken place with the server")


while True:
  cmd = input("Input: ")
  if len(cmd) == 0: break
  cli.sendall(cmd.encode())  # encode() needed for Python3
  ans=cli.recv(1024)
  # what happens if you use "4" instead of "1024" in cli.recv()?
  # try it out, send a long string to the server e.g 1234567890 and
  # then send another  string, eg abcdef
  # what are the consequences? 
  print ("Output: {up:s}".format(up=ans.decode())) # decode() needed for Python3


print("about to close the connection")
cli.close()
