class Stack:

	def __init__(self):
		self.items = []

	def is_empty(self):
		return not self.items

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def __str__(self):
		return str(self.items)

	def length(self):
		return len(self.items)

if __name__ == "__main__":

	s = Stack()
	print(s.is_empty())

	s.push(3)
	print(s)

	s.push(7)
	s.push(9)
	print(s)

	s.pop()
	print(s)

	print(s.peek())
				