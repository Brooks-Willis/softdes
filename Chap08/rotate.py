"""Written as a solution to a problem in "Think Python"
by Allen Downey

Author: Brooks Willis
"""

def rot_letter(s,n):
	"""Rotates a single letter by n spaces (ROT-n)

	s: string with one element
	n: integer
	"""
	if s.islower():
		ind = ord('a')
	elif s.isupper():
		ind = ord('A')
	else:
		print s + " isn't a letter."

	c = (ord(s) - ind + n) % 26 +ind #I must admit, I needed to look at allen's code to get the % part of this

	return chr(c)

def rotate_word(s,n):
	"""ROT encodes a given word by offset n
    
    s: alphabetical string
    n: integer
	"""
	new_word = ''
	for c in s:
		new_word += rot_letter(c,n)

	return new_word

print rotate_word('cheer', 7)
print rotate_word('melon', -10)
print rotate_word('sleep', 9)

