"""Created as a solution to an excersize in 
thinkpython by Allen Downey

Written by Brooks Willis

Creates a grid in the terminal of size x by y
"""

def print_horiz(a):
	print '+ - - - - '*a + '+'

def print_vert(a):
	print '|         '*a + '|'

def print_plus():
	print '+'

def print_pipe():
	print '|'

def print_grid(x,y):
	"""Prints a grid of size x y to the terminal

	x: number of blocks horizontally
	y: number of blocks vertically
	"""
	for z in range(0, y):
		print_horiz(x)
		print_vert(x)
		print_vert(x)
		print_vert(x)
		print_vert(x)

	print_horiz(x)


print_grid(5,4)