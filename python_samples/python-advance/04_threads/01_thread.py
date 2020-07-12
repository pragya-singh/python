from time import sleep
from threading import *

class message_printer(Thread):

	def __init__(self, message):
		Thread.__init__(self)
		self.message = message

	def run(self):
		for i in range(1,20):
			print(self.message)
			#sleep(1)


t1 = message_printer('Hello')				
t2 = message_printer('Hi')

t1.start()
t2.start()				