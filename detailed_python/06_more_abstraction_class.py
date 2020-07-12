'''
Class is another level of abstration.
Contains two things: Attributes and methods

Three important aspects bringing classes:
- Polymorphism
- Inheritence
- Encapsulation
''' 

# Inheritence
class Parser:

	def parse(self, path):
		pass

class XmlParser(Parser):

	def parse(self, path):
		print(f'Parsing XML file at path = {path} and preparing Records')


class TextParser(Parser):

	def parse(self, path):
		print(f'Parsing Text file at path = {path} and preparing Records')

xmlParser = XmlParser()
xmlParser.parse('~/in.xml')		

txtParser = TextParser()
txtParser.parse('~/in.txt')

# Polymorphism
class DbFactory:
	
	parsers = {'xml': XmlParser(), 'txt': TextParser()}

	@classmethod
	def writeToDb(cls, inFile):
		if inFile[-3:-1] == 'xml':
			DbFactory.prepareRecords(cls.parsers['xml'], inFile)
		else:
			txtParser = TextParser()
			DbFactory.prepareRecords(cls.parsers['txt'], inFile)
		print('Writing to DB')	

	# Polymorphic call	
	@staticmethod	
	def prepareRecords(parser, inFile):
		parser.parse(inFile)


DbFactory.writeToDb('~/in.xml')
DbFactory.writeToDb('~/in.txt')

# Encapsulation
class Records:

	def __init__(self, dict):
		head_record = ['Index']
		temp_data = []
		data_records = []
		for k in dict:
			head_record.append(k)
			temp_data.append(dict[k])

		for index in range(len(temp_data[0])):
			data_records.append([])
			data_records[index].append(index)
			for k in dict:
				data_records[index].append(dict[k][index])
		self.records = (head_record, data_records)	

	def __str__(self):
		out = '|'+'|'.join(self.records[0])+'|\n'

		for record in self.records[1]:
			out += '|'+'|'.join([str(item) for item in record])+'|\n'

		return out	

data = {'year':['2014', '2015', '2016', '2017', '2018', '2019'], 'sales': ['1000', '2000', '3000', '4000', '5000', '6000']}
records = Records(data)
print(records)

'''
Few Important functions:
callable(object) -> Whether the object is callable or not. Like
					function and method.
getattr(object, name[, default]) -> To get the value of an attribute
setattr(object, name, value) -> To set attribute of an object
hasattr(object, name)
issubclass(A,B)
random.choice(sequence)
type(object)
'''

print(type(records))

'''
To define an abstract class and abstract methods we have to 
do following. But it is mandatory to do as follows for shake of 
implementation. But as other languages have concept of Interfaces
or abstract class, in Python also we can have abstract class which
cannot be instantiated.
'''
from abc import ABC, abstractmethod

class Iterator(ABC):

	@abstractmethod
	def hasNext():
		pass

	@abstractmethod	
	def next():
		pass		

class ListIterator(Iterator):

	def __init__(self, l):
		self.l = l
		self.count = 0

	def hasNext(self):
		return self.count < len(self.l)
			
	def next(self):
		o = self.l[self.count]
		self.count += 1
		return o
		


iterator = ListIterator(list(range(10)))
while(iterator.hasNext()):
	print(iterator.next())

# Following will give error because abstract class cannot be
# instantiated
iterator1 = Iterator()





