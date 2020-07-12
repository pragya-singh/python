'''
==================== Dictionary ====================

Definition:
-----------
Dictionay is a built-in data structure in Python. 
It is a mapping data structure, where a value is 
mapped to a key. It can be useful in many scenarios
where list are not that useful.  

Dictionary data structure contains unique keys and 
value corresponsing to key. Values need not be unique.
'''

# ==================== Construct ====================
# Direct construction
employee_data = {'name':'Gaurav Singh', 'phone': '091-9945999459'}
# Using dict class
employee_data1 = dict({'name':'Gaurav Singh', 'phone': '091-9945999459'})
# Dictionary is nothing but pair of items. Hence can
# be constructed as follows
items = [('name','Gaurav Singh'), ('phone','091-9945999459')]
employee_data2 = dict(items)

# All following give the same outcome. Only the way 
# dictionary is constructed is different.
print(employee_data)
print(employee_data1)
print(employee_data2)

# =========== Access, Add, Delete keys ==============
# Access
print(employee_data['name']) # If key does not exist, gives error.
print(employee_data.get('name')) # To avoid error, it should be used.

# Add
employee_data['address'] = 'Whitefield'
print(employee_data)

# Delete
del employee_data['address']
print(employee_data)

'''
==================== Iteration ====================
Unlike list where if we iterate through Dictionary,
it will be the key which is iterated through. But in
case of list it is value.

Iteration with the pair of key and value is also 
possible.
'''

for key in employee_data1:
	print(key)

for key, value in employee_data2.items():
	print(f'{key}={value}')

'''
================= String Formating =================
Dictionary is very useful in cases of String 
formatting.
'''

print('New employee emp_name={name}, phone_no={phone} has joined.'.format_map(employee_data2))

'''
================= Dictionary Built-In Methods =================
Following are few useful dictionary functions
- dict.clear(): Makes the dictionary empty. Does not return 
				anything. 
- dict.copy(): Copies the original dictionary and assigns to new
               one.
- dict.deepcopy(): Similar to copy, but changing the value of one
				   does not affect other dictionary value.
- dict.get(key): To access a value corresponding to key. Returns
				 None if key does not exist.
- dict.items(): Returns the tuple(key, value pair) list.
- dict.keys(): Returns all keys of dictionary.
- dict.values(): Returns all values of dictionary.
- dict.pop(key): Removes the key and value pair. 
- dict.popItem(): Removes the first item(key, value pair) of dictionary.
'''