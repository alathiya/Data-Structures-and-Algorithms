#items = ['apple','orange','banana','apple','orange','pear','banana','pear', 'apple', 'pear', 'orange']

#counter = dict()

#for key in items:
#	if (key in counter.keys()): 
#		counter[key] +=  1
#	else: 
#		counter[key] = 1
		

#print(counter)

items = [65, 12, 4, 58, 93, 78, 24, 16, 9, 88, 91, 46]

def findmax(items): 

	if len(items) == 1: 
		return items[0]

	op1 = items[0]
	op2 = findmax(items[1:])

	if op1 > op2: 
		return op1 
	else: 
		return op2


print(findmax(items))		