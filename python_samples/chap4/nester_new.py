import sys
def printLol(input_list, identation=False, level=0, fh=sys.stdout):
	for element in input_list:
		if isinstance(element, list):
			printLol(element, identation, level+1, fh)
		else:
			if identation:
				for i in level:
					print("\t", end="", file=fh)
			print(element, end="", file=fh)