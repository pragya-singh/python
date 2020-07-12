from threading import *

def loop_sum(a,b):
	for i in range(20):
		print(a+b)

def loop_mul(a,b):
	for i in range(20):
		print(a*b)
'''
	Simple logic to run many functions as parallel threads
'''
t1 = Thread(target=loop_sum, args=(2,3))
t2 = Thread(target=loop_mul, args=(2,3))
t1.start()
t2.start()

t1.join()
t2.join()

print('main')