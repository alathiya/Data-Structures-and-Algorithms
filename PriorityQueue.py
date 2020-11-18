import heapq 

class PriorityQueue:

	def __init__(self):
		self.elements = []

	def is_empty(self):
		return not self.elements

	def put(self, item, priority):
		heapq.heappush(self.elements, (priority, item))

	def get(self):
		return heapq.heappop(self.elements)[1]

	def __str__(self):
		return str(self.elements)

if __name__== "__main__":

	pq = PriorityQueue()

	print(pq.is_empty())

	pq.put('A', 4)
	pq.put('B', 6)
	pq.put('C', 2)
	pq.put('D', 1)

	print(pq)

	print(pq.get())
	print(pq.get())

	print(pq)	

			