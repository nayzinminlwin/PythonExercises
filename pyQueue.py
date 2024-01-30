class Queue :
	def __init__(self):
		self.items = []

	def is_Empty(self):
		return self.items == []

	def peek(self):
		return self.items[len(self.items)-1]

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

# q = Queue()
# q.enqueue(6)
# q.enqueue('Cat')
# q.enqueue(True)
# print(q.size())
# print(q.dequeue())
# print(q.dequeue())
# print(q.size())