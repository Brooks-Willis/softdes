def print_horiz(a):
	print '+ - - - - '*a + '+'

def print_vert(a):
	print '|         '*a + '|'

def print_plus():
	print '+'

def print_pipe():
	print '|'

def print_grid(x,y):
	for z in range(0, y):
		print_horiz(x)
		print_vert(x)
		print_vert(x)
		print_vert(x)
		print_vert(x)

	print_horiz(x)


print_grid(5,4)