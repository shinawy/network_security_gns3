import os
import time
import random
loop=2

for i in range(1,loop+1):
    if os.fork()==0:
        time.sleep(random.randint(0,5))
        c_id=os.getpid()
        p_id=os.getppid()

        print("{}CHILD i={}, Process id ={}; parent process id={}".format("**"*i,i, c_id,p_id))
    
    else:
        c_id=os.getpid()
        p_id=os.getppid()
        print("{}PARENT i={}, Process id ={}; parent process id={}".format("++"*i,i, c_id,p_id))


