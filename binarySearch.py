def binarysearch(item, item_list): 
	
	lower = 0 
	upper = len(item_list) -1


	while lower <= upper: 

		midpt = (lower + upper) // 2

		if item_list[midpt] == item:
			return midpt 

		if item > item_list[midpt]: 
			lower = midpt + 1
		else: 
			upper = midpt - 1

	if upper > lower: 

		return None 

def is_sorted(item_list):

	#for i in range(len(item_list)-1):
	#	if item_list[i] > item_list[i+1]:
	#		return False

	return all([item_list[i] <= item_list[i+1] for i in range(len(item_list)-1)])	

	#return True


def main(): 
	item_list = [2, 8, 15, 24, 68, 79, 98, 105]
	
	#print(binarysearch(24, item_list))
	#print(binarysearch(68, item_list))
	#print(binarysearch(105, item_list))
	
	item_list1 = [4,6,7,8,1,5]

	print(is_sorted(item_list))
	print(is_sorted(item_list1))


if __name__ == "__main__":
	main()