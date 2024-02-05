"""
Example of multithreaded application using the
threading module and a lock to synchronize
access to a global variable
"""
import threading,time

THREADS=10
INCREMENTS=50000

a_lock=threading.Lock()
a=0

class IncrementingThread(threading.Thread):
    
    def __init__(self,increments):                
        threading.Thread.__init__(self)
        self.increments=increments

    def run(self):
        global a
        print ("{} starting processing".format(self.getName()))
        for i in range(0,self.increments):
            a_lock.acquire()
            a += 1
            a_lock.release()
        print("\n{} completed processing ".format(self.getName()))
        
running=[]        
for i in range(0,THREADS):
    m=IncrementingThread(INCREMENTS)
    print("=> launching {} NOW:".format(m.getName()))
    m.start()
    running.append(m)

[m.join() for m in running]



print("Excepted value: {}".format(THREADS*INCREMENTS))
print ("Obtained value: {}".format(a))
