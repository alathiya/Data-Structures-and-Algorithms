def bubblesort(dataset):
	for i in range(len(dataset)-1, 0, -1):
		for j in range(i): 
			if dataset[j] > dataset[j+1]:
				temp = dataset[j]
				dataset[j] = dataset[j+1]
				dataset[j+1] = temp
		print("Steps " + str(i), dataset)

	return dataset					
	

def main():
	list_items = [87, 65, 78, 39, 40, 4, 10, 29]
	result = bubblesort(list_items)
	print(result)


if __name__ == "__main__":
	main()