import pickle
import nester_new
"""
<Problem Statement> 
Read a file sketch.txt. Get the line spoken 
by man and other. Write it to separate files. Content would be
written as binary. Use pickle module.

<Working Description>
Using pickle module of python. It is used to dump data in bytes.
And load data back to program.
Example: 
	pickle.dump function is used to dump the data. It can throw
	a runtime exception PickleError which should also be taken 
	care of!!

"""
man=[]
other=[]
new_man=[]
try:
	with open("sketch.txt") as input, open("man_data_byte.txt","wb") as man_data, open("other_data_byte.txt","wb") as other_data:
		for line in input:
			try:
				(person, line_spoken)=line.split(":",1)
				if person == "Man":
					man.append(line_spoken)
				else:
					other.append(line_spoken)
			except ValueError:
				pass
		pickle.dump(man,man_data)
		pickle.dump(other,other_data)	
	with open("man_data_byte.txt","rb") as new_man_file:
		new_man=pickle.load(new_man_file)
		nester_new.printLol(new_man)	
except IOError as err:
	print("File Error : "+str(err))
except pickle.PickleError as err:
	print("Pickling Error : "+str(err))
except EOFError as err:
	print("EOFError : "+str(err))