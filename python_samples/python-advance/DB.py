import os
import json
import time
import pickle

class DB:

	def __init__(self):
		self.path = '/Users/singg/Desktop/KV/'
		self.offset = {}
		self.load()

	def insert(self, k, value):
		content = bytes(json.dumps(value), 'UTF-8')
		l = len(content)

		if k in self.offset:
			return False

		with open(self.path+os.path.sep+str(k % 10), 'ab+') as file:
			file.write(content)

		with open(self.path+os.path.sep+str(k % 10), 'rb') as file:
			b = file.read()
			self.offset[k] = (len(b) - l, l)

		return True	

	def read(self, k):
		b = None
		with open(self.path+os.path.sep+str(k % 10), 'rb') as file:
			file.seek(self.offset.get(k)[0])
			b = file.read(self.offset.get(k)[1])
		return b.decode('UTF-8')

	def load(self):
		if os.path.exists('/Users/singg/Desktop/KV/keys.pkl'):		
			with open('/Users/singg/Desktop/KV/keys.pkl', 'rb') as f:
				self.offset = pickle.load(f)

	def store(self):
		with open('/Users/singg/Desktop/KV/keys.pkl', 'wb') as f:
			pickle.dump(self.offset, f, pickle.HIGHEST_PROTOCOL)

	def delete(self, k):
		os.remove(self.path+os.path.sep+str(k))	


def f(n):
 		output = 0
 		if n > 0:
 			output = 1
 		return output

if __name__ == "__main__":

	db = DB()

	#t0 = time.time()
	#for i in range(1,1000000):
	#	db.insert(i, {'name':'name'+str(i), 'designation':'MTS-'+str(i)})

	keys = [f(i)*10**i+1 for i in range(0, 6)]	
	#t1 = time.time()	
	#for k in keys:
	#	t2 = time.time()
	#	print(db.read(k))	
	#	t3 = time.time()
	#	print(f"Time Taken to Read key {k} = {t3-t2}")
	
	key = int(input('Enter Key:'))
	t2 = time.time()
	print(db.read(key))
	t3 = time.time()
	print(f"TIME_TAKEN={t3-t2}")

	#print(f"Time Taken to Insert 1000 key and values={t1-t0}")
	#db.store()
 	



	

