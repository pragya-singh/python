
'''
Module does multiple maths operations 	
'''

def square(x):
 ''' 
 Returns square of a given number
 >>> square(2)
 4
 >>> square(3)
 9
 '''
 return x*x

def product(x, y):
 ''' Product of two numbers '''
 return x*y

def product1(x, y):
 ''' Product with error '''
 if x == 7 or y ==9:
  return 'An error has occured'
 else:
  return x*y
	
if __name__ == "__main__":
 import doctest, my_math
 doctest.testmod(my_math)
