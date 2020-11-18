def functionfilter(x):
	if x % 2 == 0:
		return True   

def functionmap(x):
	return x**2   


def main(): 

	lst = [4, 6, 2, 8, 9, 1, 7, 5]

	#print(list(filter(functionfilter, lst)))
	
	#print(list(map(functionmap, lst)))

	print(list(map(lambda x: x**2, lst)))		


if __name__=="__main__": 

	main()