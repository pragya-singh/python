# List & Tuples are workhorse of python

# Sequence Data Structure is indexed. Index are 0,1,2,...
# Index represent the offset from first element.

# ================= List =======================
# List is a mutable built-in sequence. 

# =============== Operations on List ===========
# Indexing
# Slicing
# Addition
# Multiplication
# Checking Membership
# Built-In functions : 
#	To check the size of list
#   To check min/max elements in list

# Indexing

numbers = [0,1,2,3,4,5,6,7,8,9]
print('===============INDEXING===============')
print(f'Number at 0={numbers[0]}, at 1 = {numbers[1]}')

# Slicing
'''
Slicing can be done on list and it is very useful.
In case if we want to fecth only few part of a list.
eg: A list named my_list, slicing can be done as 
follows: 
	my_list[start_index, end_index]
		start_index is included in the result
		end_index is excluded in the result
		end_index should be greated than start_index
'''
numbers = [0,1,2,3,4,5,6,7,8,9]
print('===============SLICING===============')
print(f'Numbers from 0 to 5 ={numbers[0:6]}')

message = 'Python is a good language!!'
print(message[0:6])

# Slicing from backwards
'''
To get last three elements from list can be done as
follows
'''	
print(f'Last three elements={numbers[-3:]}')

# Slicing with Steps
'''
Slicing with steps can be done. Default step is 1, but we can 
define step as we need.
eg: If my_list is a list, we can slice it as follows:
my_list[start_index:end_index:step]. step is the number telling
how much to jump.
'''
print(numbers[0:10:2])
print(numbers[::2])

# Adding(Sequence Concatanation) & Multiplication of sequences
database = [['111', 'Gaurav Singh'],
			['112', 'Shubh']] + [['113', 'Vinit']]
print(database)			

empty_list = [None] * 8
print(empty_list)

# Membership
print(f'8 is element or not {8 in numbers}')
print(f'12 is element or not {12 in numbers}')

# Built-In functions
print(f'Size of list={len(numbers)}')
print(f'Maximum number in list={max(numbers)}')
print(f'Minimum number in list={min(numbers)}')

# Converting a String to list
msg = 'Hello'
print(list(msg))
print(''.join(list(msg)))

# =============== Changing/Mutating lists ===========
# list.append(element) => appends element at the end
# list.clear() => clears the list(make the list empty)
# list.copy() => Copies all elements of a list and creates a new list
# list.count(element) => Tells occurance count of an element
# this_list.extend(that_list) => this_list will also have all the elements of that_list 
# list.index(element) => gives the first index of occurance of element
# list.insert() => 
# list.pop() => Pops out the last element. If pop for first element then can be mentioned as follows : list.pop(0) 
# list.remove(element) => removes the first occurance of element
# list.reverse() => Makes the elements of list in reverse order
# list.sort() => It will sort the elements inside the list, if a new list is needed and the original list
#.               need to be maintained as it is. Then sorted_list = sorted(original) can be used.				



# =============== Advanced Sorting of list ===========
# In sort function of list two arguments can be passed.
# One is key and another is reverse. function is passed to key and reverse decides the order.
x = ['a', 'aa', 'aaaaaaaa', 'aaaa', 'aaa']
x.sort(key=len, reverse=True)
print(x)

# ================= List =======================
# Tuple is a immutable built-in sequence.
# All operations can be done same as list but mutable operations are not applicable. 
record = ('111', 'Gaurav Singh')
print(record)

# Sequence can be converted to tuple using tuple()
record1 = tuple(['111', 'Gaurav Singh'])
print(record1)