import os
import time
import random
loop=3

zelist=[]
count=0

for i in range(1,loop+1):
    if os.fork()==0:
        c_id=os.getpid()
        p_id=os.getppid()
        time.sleep(random.randint(0,5))
        zelist.append('a')
        count += 1
        print("{}CHILD i={}, Process id ={}; parent process id={}; zelist={}, count={}".format("**"*i,i, c_id,p_id,zelist,count))
    
    else:
        c_id=os.getpid()
        p_id=os.getppid()
        time.sleep(random.randint(0,5))
        zelist.append('1')
        count+=1
        print("{}PARENT i={}, Process id ={}; parent process id={}; zelist={}, count={}".format("++"*i,i, c_id,p_id,zelist,count))


print(">End of the program, zelist = {}".format(zelist))
