cursor = open("sketch.txt")
"""
Checking whether ":" is contained in a line, makes the code 
more fragile. We can use exception handling instead.
"""
"""
for line in cursor:
	if not line.find(":") == -1:
		(role,line_spoken) = line.split(":",1)
		print(role,end="")
		print(line_spoken,end="")
"""
try:
	for line in cursor:
		try:
			(role,line_spoken) = line.split(":",1)
			print(role,end="")
			print(line_spoken,end="")
		except ValueError:
			pass
except IOError:
	print("File does not exist!!")
	
cursor.close()