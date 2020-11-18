def flowerbox(list_items):

	a = 0 
	b = 0 
	
	for val in  list_items: 
		a, b = b, max(a+val, b)
		print(a,b)
	return b 

if __name__=="__main__": 
	print(flowerbox([9,10,9]))