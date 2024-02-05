"""
Producer/Consumer problem using Queue module
"""
import threading,time,queue

THREADS=10
BUFSIZE=5

#just create a queue
q=queue.Queue()

class Reader(threading.Thread):
	
	def run(self):
		job=""
		
		while job!=None: 
			#thread terminates when the producer sends None
			
			#wait for content
			job=q.get()
			
			if job!=None:
				print("{}: {}".format(self.getName(),job))
				#slow down things a bit
				time.sleep(1)
				
			#notify the queue that you have done your job
			q.task_done()
				
		print("{}: I'm done!".format(self.getName()))
				
			

class Producer(threading.Thread):
	
	def run(self):
		while True:
			#fetch input from the command line
			job=input("Input: ")
			
			if job!="":
				#wait for the queue to be empty
				q.join()
				#insert the elements
				[q.put(c) for c in job]
			else:
				#send a None to each thread to let them know
				#we are done.
				[q.put(None) for i in range(THREADS)]
				break
			

readers=[Reader(name="reader_%d"%i) for i in range(THREADS)]		
producer=Producer(name="producer")

#start threads...
[m.start() for m in readers+[producer]]
#...and join them
[m.join() for m in readers+[producer]]
