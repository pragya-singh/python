

try:
	x = input('Numerator=')
	y = input('Denominator=')

	o = x/y
except (ZeroDivisionError, TypeError):
	print('Denominator is 0')	

	
try:
	x = input('Numerator=')
	y = input('Denominator=')

	o = x/y
except ZeroDivisionError as e:
	print('Error = '+str(e))
except TypeError as e:
	print('Wrong input formant '+str(e))


try:
	x = input('Numerator=')
	y = input('Denominator=')

	o = x/y
except Exception as e:
	print('Error = '+str(e))


class ParseException(Exception):
	pass


try:
	x = input('Numerator=')
	y = input('Denominator=')

	o = x/y
except Exception as e:
	raise ParseException	