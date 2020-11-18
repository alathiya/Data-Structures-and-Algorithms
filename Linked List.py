class Node: 

	def __init__(self, data):
		self.data = data
		self.next = None

class Linkedlist:

	def __init__(self):
		self.head = None

	def printlist(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next 

	def push(self, new_data):
		new_node = Node(new_data)

		new_node.next = self.head
		self.head = new_node 

	def insertAfter(self, prev_node, new_data):
		
		if prev_node is None: 

			print("Prev node must be linked list")

		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def append(self, new_data):
		
		new_node = Node(new_data)

		if self.head is None:
			self.head = new_node
			return 

		last = self.head 
		while(last.next):
			last = last.next

		last.next = new_node 
			


if __name__=='__main__':

	llist = Linkedlist()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second;
	second.next = third 

	llist.printlist() 

	llist.push(7)

	llist.printlist()

	llist.insertAfter(llist.head.next, 8)	 
	
	llist.printlist()

	llist.append(9)

	llist.printlist()	