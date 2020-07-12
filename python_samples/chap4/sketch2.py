import nester_new
"""
<Problem Statement> 
Read a file sketch.txt. Get the line spoken 
by man and other. Write it to separate files. Each file should contain
one line spoken in a separate line.

<Working Description>
Sketch2.py also does the same functionality what sketch1.py does, the
difference writes data to files not directly in string format of list
data structure. But it writes each element in the list as a different 
line to file. For that nester module has been modified. Which has an 
extra optional argument fh=sys.stdout.

<Note>
with open() is used to get rid of finally block and closing the file 
code.
"""
man=[]
other=[]

try:
	with open("sketch.txt") as data, open("man.txt","w") as man_file,open("other.txt","w") as other_file:
		for line in data:
			try:
				(person, line_spoken) = line.split(":",1)
				if person == "Man":
					man.append(line_spoken)
				else:
					other.append(line_spoken)
			except:
				pass
		nester_new.printLol(man,fh=man_file)
		nester_new.printLol(other,fh=other_file)
except IOError as err:
	print("File Error : "+str(err))


def func():
	print("func")	
