"""
How variables are passed when forking
(Python3 syntax)
"""
import time
import os

mylist=["a", "b"]
print("beginning, mylist: {}, id(mylist): {}".format(mylist, id(mylist)))

if os.fork()==0:
        while True:
               mylist.append("1")
               print("child, mylist: {} id(mylist): {}".format(mylist, id(mylist)))
               time.sleep(2)
else:
        while True:
               mylist.append("X")
               print("parent, mylist: {} id(mylist): {}".format(mylist, id(mylist)))
               time.sleep(2)        



