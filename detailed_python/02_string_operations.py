# String is character sequence

# All operations can be done with the String except mutation operation.
# That means indexing, concatanation, len(), min(), max() can be done on 
# string as well. But assigning a new value to a character is not possible.

# String Formatting
# There are following ways we can format string 

# Using Conversion Specifiers
employee_record = (123, 'Gaurav', 'Singh')
message = 'Employeed details are as follows ID=%s, FIRST_NAME=%s, LAST_NAME=%s'
print(message % employee_record)

# Using format function
message1 = 'Employeed details are as follows ID={}, FIRST_NAME={}, LAST_NAME={}'.format(employee_record[0], employee_record[1], employee_record[2])
print(message1)

# Another and easier way to use format function
message2 = f'Employeed details are as follows ID={employee_record[0]}, FIRST_NAME={employee_record[1]}, LAST_NAME={employee_record[2]}'
print(message2)

# Another way to use conversion specifiers or format function to show fractions to particular digit.
from math import pi
pi_tuple = ('pi', pi)
print('Value of %s=%.2f' % pi_tuple)
print('Value of {}={:.2f}'.format(pi_tuple[0], pi_tuple[1]))
print(f'Value of {pi_tuple[0]}={pi_tuple[1]:.2f}')

# Many methods in string are inherited from string module 
# which was there in previous version of python. The functions 
# are very helpful.

# str.find(sub_string): Returns index of first occurance of sub_string
# str.lower(): lowercase conversion
# str.upper(): uppercase conversion
# str.split(): Returns list of words, delimiter is SPACE. Delimiter can be specified
# str.join(list): Concatanates the elements of list by specified join string. It is just 
#                 reverse of split				
# str.strip(): Gives a new string with removed whitespace from both left and right
# str.lstrip(): Gives a new string with removed whitespace from left
# str.rstrip(): Gives a new string with removed whitespace from right
# str.replace(str_to_be_replaced, replacement_string): Returns a new string with replaced value.
# str.translate(table): Returns a new string with replaced characters mentioned in table. It is 
#						much more efficient function to replace charaters in whole document. 
#					    For example replacing \n character from whole document. A table needs to
# 						be created first before translation.					 

# find()
statement = 'Python is an interesting programming language.'
print(statement.find('language'))
#split()
tokens = statement.split()
print(tokens)
#join()
print(' '.join(tokens))

# strip()
sentence = '   Hello Python    '
print(sentence.strip())

english_statement = 'Python is an incredible programming language.'
table = str.maketrans('cs', 'kz') # c replaced with k and s replaced with z
print(table)
german_statement = english_statement.translate(table)
print(german_statement)


# There are plenty of functions which starts with is. eg: isspace, isdigit, isnumeric etc.
# They are again taken from string module of python2
