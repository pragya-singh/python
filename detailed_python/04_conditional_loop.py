'''
Conditional, loop and other statements
are similar to other languages even in python.

There are few differences:

New block starts with : and then next line should 
have indentation.
'''

if True:
	print('Running the True block')
else:
	print('Running False block')


for item in range(10):
	print(item)

'''
List comprehension is a good short hand for doing the 
loop calculation in one line.
'''
square = [x*x for x in range(10)]
print(square)		


i = 10
while i > 0:
	print(i)
	i -= 1

print('f(x)=x*x')
print('='*10)
for num, sq in list(zip(list(range(10)), square)):
	print(f'{num}->{sq}')


'''
exec() function can be used to run any python statement
within a given scope or global scope. But it is not very
safe, mainly in case of network programming.
'''
from math import sqrt

scope = {}
exec('sqrt=1',scope)
print(sqrt(4))
print(scope['sqrt'])
print(list(scope.keys()))	


'''
eval() function can be used to evaluate python expression
within a given scope or global scope. But it is not very
safe, mainly in case of network programming.
'''

print(eval('18*2+3'))

scope1 = {}
scope1['x'] = 2
scope1['y'] = 3

print(eval('x*y', scope1))