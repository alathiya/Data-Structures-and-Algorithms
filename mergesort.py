def mergesort(dataset): 
	if len(dataset) > 1: 

		mid = len(dataset) // 2
		leftarr = dataset[:mid]
		rightarr = dataset[mid:]

		mergesort(leftarr)
		mergesort(rightarr)

	
		i = 0
		j = 0
		k = 0 

		while i < len(leftarr) and j < len(rightarr):
			if leftarr[i] < rightarr[j]: 
				dataset[k] = leftarr[i]
				i = i + 1
			else:
				dataset[k] = rightarr[j]
				j = j+1	
			k=k+1

		if i < len(leftarr): 
			dataset[k] = leftarr[i]
			i = i + 1
			k = k + 1
	
		if j < len(rightarr): 
			dataset[k] = rightarr[j]
			j = j + 1
			k = k + 1	

	return dataset


def main(): 
	list_items = [56, 89, 24, 65, 32, 14, 75, 49, 67]
	print (list_items)
	mergesort(list_items)
	print(list_items)
	


if __name__ == "__main__":
	main()
	
