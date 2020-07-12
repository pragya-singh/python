import pickle
from athletelist import AthleteList

def read_file(file_name):
	try:
		with open(file_name) as data:
			line = data.readline()
			values = line.strip().split(",")
			return AthleteList(values.pop(0), values.pop(0), values)
	except IOError as err:
		print("File Error : "+ str(err))
		return None


def put_to_store(files_list):
	all_athletes = {}
	for file_name in files_list:
		athlete = read_file(file_name)
		all_athletes[athlete.name] = athlete
	try:
		with open("athletes.txt","wb") as athletes_data_file:
			pickle.dump(all_athletes,athletes_data_file)			
	except IOError as err:
		print("File Error : "+str(err))
	return all_athletes


def get_from_store():
	try:
		with open("athletes.txt","rb") as athletes_data_file:
			all_athletes = pickle.load(athletes_data_file)
	except IOError as err:
		print("File Error : "+str(err))
	return all_athletes

#james = read_file("james2.txt")
#print(james.name+"'s top three times = "+str(james.top3()))

#put_to_store(["james2.txt","julie2.txt","mikey2.txt","sarah2.txt"])
#all_athletes = get_from_store()

#print(all_athletes)



