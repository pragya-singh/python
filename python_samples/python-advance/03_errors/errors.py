# There are following types of errors which we encounter:
# - Compile Time Error(e.g. missed a colon, but code will break at starting)
# - Logical Error(e.g. Wrong logic, but code works)
# - Run Time Error(e.g. There are some specific scenarios when at some error,
#   application stopped working because of error.)

a = 5
b = 2

try:
	print('Resource Openned')
	c = a/b
	print(c)
	k = int(input('Enter a value:'))
except ZeroDivisionError:
	print('You cannot divide a number by 0')
except Exception as e:	
	print('Something went wrong', str(e))
finally:
	print('Resource Closed')

