"""
Producer/Consumer problem using condition variables
"""
import threading,time

THREADS=10
BUFSIZE=5

work_buffer=""
work_buffer_cond=threading.Condition()

class Reader(threading.Thread):
    
    def run(self):
        global work_buffer
        job=""
        
        while job!=None: 
            #thread terminates when the producer sends None
            
            #wait for content
            work_buffer_cond.acquire()
            while work_buffer!=None and len(work_buffer)==0:
                print("{}: about to wait".format(self.getName()))                                
                work_buffer_cond.wait()
                print("{}: awaken".format(self.getName()))
                                
            
            #remove the first character from the string buffer
            if work_buffer!=None:
                job=work_buffer[0]
                work_buffer=work_buffer[1:]
            else:
                job=None
            #signal to everybody that the buffer has changed
            work_buffer_cond.notifyAll()
            work_buffer_cond.release()
            
            if job!=None:
                print("{}: {}".format(self.getName(),job))
                #slow down things a bit
                time.sleep(1)
                
        print("{}: I'm done!".format(self.getName()))
                
            
class Producer(threading.Thread):
    
    def run(self):
        global work_buffer
        job=""
        while job!=None:
            #fetch input from the command line
            job=input("Input: ")
            
            #termination condition is empty string
            job=job if job!="" else None
            
            #try to dispatch it to workers
            work_buffer_cond.acquire()
            while len(work_buffer)>0:
                work_buffer_cond.wait()
                                
            
            work_buffer=job
            #signal to everybody that the buffer has changed
            work_buffer_cond.notifyAll()
            work_buffer_cond.release()

readers=[Reader(name="reader_%d"%i) for i in range(THREADS)]        
producer=Producer(name="producer")

#start threads...
[m.start() for m in readers+[producer]]
#...and join them
[m.join() for m in readers+[producer]]
