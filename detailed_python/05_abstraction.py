'''
Function: Are defined by def keyword.
'''

'''
If need to keep documentation for a given function in python, 
the documentation given just below the function name will 
be captured as documentation for that function.
'''
def square(n):
	'''Returns square for a given number'''
	return n*n

print(square.__doc__)	

'''
In Python whether we return some value from function
or not, in both cases it is called a function. But in
language like Pascal, those blocks which dont return 
any value are called Procedures.
'''
def test():
	print('Before Returen Statement')
	return
	print('After Return Statement') # This will not be executed, because it is after return

test()

'''
==================================================================
Affect of function on variables
==================================================================
Functions dont change Immutable variables which are changed within
the function. Following example Tells it.
'''
i = 0
def increament(p):
	n = p
	n += 1
	print(n)

increament(i)
print(i)

'''
Since i is immutable hence function increament() does not increament
the variable i, which is outside the function. If we really want to
increament the variable, we have to reassign the increamented returned 
value to i. As follows:
'''
def increament1(p): return p+1

i = increament1(i)
print(i)

'''
Immutable variable can be modified if there is a change in a variable 
within a function as follows.
'''
l = []
def init_values(lst):
	lst.append(None)

init_values(l)
print(l)

'''
The above can be understood as follows. As we have removed the function
but following happens under the hood.
'''	

count = 0
num = count
num += 1
print(num)
print(count)

my_list = []
mod_list = my_list
mod_list.append(None)
print(mod_list)
print(my_list)

'''
============================================================================
Keyword parameters and positional parameters
============================================================================
Keyword Parameter is very useful, because even if developer misses the order,
the name of the parameter will take care of passing the right value. Another
benifit is, it explains the meaning of the parameter which is being passed.
Otherwise sometimes it is difficult to understand what is the meaning of 
parameter.
'''

def profile(name, date, month, year):
	return {'name':name, 'dob': f'{date}-{month}-{year}'}


print(profile('Stuti', '02', '09', '2000'))
print(profile('Stuti', '02', year='2000', month='09'))
print(profile(name='Stuti', month='09', year='2000', date='02'))

'''
============================================================================
Collecting multiple parameters
============================================================================
'''

# For collecting list of parameters and un-packing them
def apply_operation(oper, *numbers):
	return [oper(x) for x in numbers]

print(apply_operation(lambda x: x*x, 1,2,3,4,5,6))
print(apply_operation(lambda x: x*x, *list(range(10))))

# For collecting key value parameters and un-packing them
def store_data(**employee):
	print('storing data...')
	print(employee)
	print('Data Stored')

store_data(name='AB Devilliars', dob='05-09-1980')


'''
============================================================================
Scope/Namespace
============================================================================
The variables defined in a program has a scope. Scope can be considered as a
map, which contains variables and their values. Each function has its own
local scope(closure). The variables defined in a function can be accessed 
within the scope of the function and not outside. But a gobal variable can be
accessed within a function.
But a variable named same as global variable within a function is shadowed by
the value defined locally and not globally.
'''

# Following example shows that the variable defined with same name as global
# variable does not do anything with the global variable. And hence the value
# of global x remains same as 1
x = 1
def function():
	x = 2
	print(f'x inside the function={x}')

function()
print(f'x outside the function={x}')	

# Following example shows that the variable global variable is accessible 
# within local scope of the function
def function1():
	 return x+1

print(f'x outside the function={function1()}')

# But if we really want to use the global varaible to be used inside the 
# function with the same name inside the function it should be used as 
# follows
def function2():
	global x
	x = x + 1


function2()
print(f'x outside the function={x}')	

'''
Variable defined in outer function can be used within the scope 
inner function. i.e.: multiplyByFactor contains the factor varibale 
within its scope which is called 'Closure'.
'''
def multiplier(factor):
	def multiplyByFactor(number):
		print(vars())
		return number * factor
	return multiplyByFactor

# multipler(2) returns a function which contain factor=2 within it's
# scope
double = multiplier(2)
double(5)

# multipler(3) returns a function which contain factor=3 within it's
# scope
triple = multiplier(3)
triple(5)

# multipler(10) returns a function which contain factor=10 within it's
# scope
multiplier(10)(3)	

'''
Recursion
'''
def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)	

print(factorial(6))


def binary_search(sorted_sequence, start=0, end, item):
	if start == end and sorted_sequence[start] != item:
		return -1

	m = (start+end)//2
	if item > sorted_sequence[m]:
		return binary_search(sorted_sequence, m+1, end, item)
	elif item < sorted_sequence[m]:
		return binary_search(sorted_sequence, start, m, item)
	elif item == sorted_sequence[m]:
		return m		

seq = [100, 67, 99, 12, 55, 79, 9]
l = sorted(seq)
print(l)
print(binary_search(l, start=0, end=len(l)-1, item=99))


