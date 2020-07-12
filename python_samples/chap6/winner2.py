from athletelist import AtheleteList

def read_file(file_name):
	try:
		with open(file_name) as data:
			line = data.readline()
			items = line.strip().split(",")
			return AtheleteList(items.pop(0),items.pop(0),items) 
	except IOError as err:
		print("File Error : "+str(err))
		None

james = read_file("james2.txt")
print(james.name+"'s fastest time are:"+str(james.top3()))

julie = read_file("julie2.txt")
print(julie.name+"'s fastest time are:"+str(julie.top3()))

mikey = read_file("mikey2.txt")
print(mikey.name+"'s fastest time are:"+str(mikey.top3()))

sarah = read_file("sarah2.txt")
print(sarah.name+"'s fastest time are:"+str(sarah.top3()))