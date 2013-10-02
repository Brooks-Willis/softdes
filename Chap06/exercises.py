"""Created as a solution to an excersize in 
thinkpython by Allen Downey

Written by Brooks Willis
Contains is_power, which determines if one int is a power of another,
and gcd, which computed the greatst common divisor of two integers
"""

from math import *

def is_power(a,b):
	"""Determines if a is a power of b

	a: Positive integer (larger than b)
	b: Positive integer
	"""
	if a < b:
		return False
	elif a % b == 0 & is_power(a/b,b):
	    return True
	else:
		return False

def gcd(a,b):
	"""Finds the greatest common divisor of a and b

	a: Positive integer
	b: Positive integer
	"""
	if type(a) != int or type(b) != int:
		return 'a and b must be integers'

	elif a < 0 or b < 0:
		return 'a and b must be positive'
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

#Test is_power
print '5**10 is a power of 5 -', is_power(5**10,5)
print '4**3 is a power of 4 -', is_power(4**3,4)
print '9 is a power of 3 -', is_power(9,3)
print '19**2 is a power of 19 -', is_power(19**2,19)
print '144 is a power of 12 -', is_power(144,12)
print '20 is a power of 20 -', is_power(20,20)
print '25 is not a power of 6 -', is_power(25,6)
print '21 is not a power of 20 -', is_power(21,20)
print '24 is not a power of 19 -', is_power(24,19)
print '7 is not a power of 11 -', is_power(7,11)

#Test gcd
print 'The gcd of 3 and 9 is', gcd(3,9)
print 'The gcd of 27 and 14 is', gcd(27,14)
print 'The gcd of 125 and 15 is', gcd(125,15)
