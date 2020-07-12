"""
	Printing elements of list recursivily.
	Input : icecreams=["amul",["flavours",["vanilla","butter scotch","black current"]]]
"""
def recList(my_list,identation=True,level=0):
#Dont know why it is failing
	for element in my_list:
		if isinstance(element,list):
			recList(element,identation,level+1)			
		else:
			if identation:
				for i in range(level):
					print('\t',end="")
				print(element)		
				
	
icecreams=["amul",["flavours",["vanilla","butter scotch","black current"]]]
recList(icecreams)