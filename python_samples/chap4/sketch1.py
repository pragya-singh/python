"""
<Problem Statement> 
Read a file sketch.txt. Get the line spoken 
by man and other. Write it to separate files.

<Working Description>
Sample program to write the data to a file. 
Content of the two lists(man,other) has been directly written
to files. 
Note: locals() is used to check whether a given data is initialized
	  in a given context or not.
"""
man=[]
other=[]
try:
	iter = open("sketch1.txt")	
	for line in iter:
		try:
			(person,line_spoken)=line.split(":",1)
			if(person=="Man"):
				man.append(line_spoken)
			else:	
				other.append(line_spoken)
		except:
			pass
			#print("Error in:"+line)
except IOError as err:
	print("File Error"+str(err))
finally:
	if iter in locals():
		iter.close()

try:
	man_file = open("man_data.txt","w")
	other_file = open("other_data.txt","w")
	print(man, file=man_file)
	print(other, file=other_file)		
except IOError:
	print("IOError")	
finally:
	man_file.close()
	other_file.close()

