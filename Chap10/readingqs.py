def main():
	print nested_sum([[1,2,3],[4,5,6,[7,8,9]])

def nested_sum(t):
	x = 0
	for val in t:
		if type(val) == int:
			x += val
		else:
			x += nested_sum(val)
		return x

def remove_duplicates(t):
	res = []
	for i in range(len(t)):
		if t[i] not in res:
			res.append(t[i])
	return res

if __name__ == '__main__': #Only run main if called from command line
	main()

