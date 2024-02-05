"""
Producer/Consumer problem using simple locks.
Notice: it's inefficient! Polling should be 
always avoided.
"""
import threading,time

THREADS=10
BUFSIZE=5

work_buffer=""
work_buffer_lock=threading.Lock()

class Reader(threading.Thread):
	
	def run(self):
		global work_buffer
		job=""
		while job!=None: 
			#thread terminates when the producer sends None
			
			#wait for content
			work_buffer_lock.acquire()
			while work_buffer!=None and len(work_buffer)==0:
				work_buffer_lock.release()
				
				#we are out of the critical region, let's sleep
				#for a little bit
				time.sleep(1)
				
				#let's get in again
				work_buffer_lock.acquire()
			
			#remove the first character from the string buffer
			if work_buffer!=None:
				job=work_buffer[0]
				work_buffer=work_buffer[1:]
			else:
				job=None
			
			work_buffer_lock.release()
			
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
			work_buffer_lock.acquire()
			while len(work_buffer)>0:
				work_buffer_lock.release()
				
				print("{}: waiting for buffer to empty".format(self.getName()))
				time.sleep(1)
				
				work_buffer_lock.acquire()
			
			work_buffer=job
			work_buffer_lock.release()

readers=[Reader(name="reader_%d"%i) for i in range(THREADS)]		
producer=Producer(name="producer")

#start threads...
[m.start() for m in readers+[producer]]
#...and join them
[m.join() for m in readers+[producer]]
