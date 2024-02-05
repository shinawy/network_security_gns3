"""
How variables are passed when forking
(Python3 syntax)
"""
import time
import os

file_desc=open("./2lines_to_read.txt", encoding='utf-8')
first_line = file_desc.readline().strip()
second_line = file_desc.readline().strip()

print("1: {}".format(first_line))
print("2: {}".format(second_line))

file_desc.seek(0)

if os.fork()==0:
        while True:
               child_line=file_desc.readline().strip()
               print("child, line read: {}".format(child_line))
               file_desc.seek(0)
               time.sleep(2)

else:
        while True:
               parent_line=file_desc.readline().strip()
               print("parent, line read: {}".format(parent_line))
               time.sleep(2)
               file_desc.close()


