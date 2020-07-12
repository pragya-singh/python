cursor = open("sketch.txt")
"""
Checking whether ":" is contained in a line, makes the code 
more fragile. We can use exception handling instead.
"""
man = []
other = []
try:
	for line in cursor:
		try:
			(role,line_spoken) = line.split(":",1)
			line_spoken = line_spoken.strip()
			if(role == "Man"):
				man.append(line_spoken)
			elif(role == "Other Man"):
				other.append(line_spoken)	
		except ValueError:
			pass
	cursor.close()
except IOError:
	print("File does not exist!!")
	

try:
	man_file = open("data.txt",'w')
	other_file = open("data_other.txt",'w')
	print(man,file=man_file)
	print(other,file=other_file)
except IOError:
	print("IOError")
finally:
	man_file.close()
	other_file.close()