"""
Simple concurrent TCP server
reading from several sockets
using select()
"""
import socket
import select

PORT=4444
HOST="192.168.2.21"

srv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
srv.bind((HOST,PORT))
srv.listen(1)

#associate each socket to its address info
clisocks={}
end="not yet"

while len(end) != 0:
     r,w,x=select.select([srv]+list(clisocks.keys()),[],[])
    
     if srv in r:
        conn,addr=srv.accept()
        print ("new connection from {}".format(addr))
        clisocks[conn]=addr
    
     for conn in [i for i in r if i!=srv]:
         print("There is something to read from {}".format(conn))
         data=conn.recv(1024)
         if data:
            conn.send(data.upper())
         else:
            print("dropped connection from {}".format(clisocks[conn]))
            clisocks.pop(conn)

     print("We have {} clients connected so far".format(len(clisocks)))
     end=input("<CR>: stop the server / any char: continue : \t")
        
# time to nicely close all the sockets
for conn in r:
        conn.close()
# Was it a good idea ? 
print("over and out")

