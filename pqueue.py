from pyQueue import Queue

class pQueue():
	def __init__(self):
		self.items = {}

	def is_Empty(self):
		return len(self.items) == 0

	def peek(self):
		return self.items{len(self.items)-1}

	def enqueue(self,item,priority=0):
		if priority not in self.items :
			self.items[priority]=Queue()

		queue = self.items[priority]
		queue.enqueue(item)
		print(item,"is priority",priority)

	def dequeue(self):
		keys = list(self.items.keys())

		if len(keys) > 0 :
			print(keys)
			keys = sorted(keys)
			print("Now Sorted keys are",keys)
			cursor = keys[-1]
			print("Now cursor index is at",keys.index(cursor))

			myqueue = self.items[cursor]
			val = myqueue.dequeue()
			print("Dequeued",val,"of priority",cursor)

			if myqueue.size() == 0:
				del self.items[cursor]
			return val

		return ""

	def size(self):
		size = 0
		for key in self.items.keys():
			size = size + self.items[key].size()
		return size


