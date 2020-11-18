from collections import deque

class Queue:

	def __init__(self):
		self.items = deque()

	def is_empty(self):
		return not self.items 

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return self.items.popleft()

	def size(self):
		return len(self.items)

	def __str__(self):
		return str(self.items) 

	def peek(self):
		return self.items[0]

if __name__ == "__main__":

	q = Queue()
	print(q)
	q.enqueue('A')
	q.enqueue('B')
	q.enqueue('C')

	print(q)

	print(q.dequeue())
	print(q.dequeue())
	
	print(q.size())
	print(q.peek())

	print(q.is_empty())


	q1 = Queue()
	q1.enqueue("Learning")
	q1.enqueue("with")
	q1.dequeue()
	q1.enqueue("Linked")
	q1.enqueue("In")
	q1.dequeue()
	print(q1)

	