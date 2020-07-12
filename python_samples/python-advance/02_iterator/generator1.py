import memory_profiler as mem_profile
import random
import time

names = ['Gaurav Singh', 'John', 'Michael', 'Yaron', 'Shankar', 'Harish', 'Nilesh']
majors = ['Electronics', 'Computer Science', 'Biotechnology', 'Mechanical', 'Civil Engineering', 'Information Technology', 'Chemical Engineering']

print(f'Memory Usage Before={mem_profile.memory_usage()}MB')
def people_list(num):
	people = []
	for i in range(num):
		student = {
			'id':i,
			'name': random.choice(names),
			'major': random.choice(majors)
		}
		people.append(student)
	return people

def people_generator(num):
	people = []
	for i in range(num):
		student = {
			'id':i,
			'name':random.choice(names),
			'major':random.choice(majors)
		}
		yield student	


#t1 = time.clock()
#all_data = people_list(1000000)
#t2 = time.clock()

t1 = time.clock()
all_data = people_generator(1000000)
t2 = time.clock()

print(f'Memory Usage After={mem_profile.memory_usage()}MB')
print(f'Time Taken={t2-t1}')