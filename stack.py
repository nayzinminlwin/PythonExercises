class Stack:

	def __init__(self):
		self.item = []

	def is_empty(self):
		return self.item == []
	
	def push(self,item):
		self.item.append(item)

	def peek(self):
		# return self.item[len(self.item)-1]
		return self.item[self.size()-1]

	def pop(self):
		return self.item.pop()

	def size(self):
		return len(self.item)

	def displayVal(self,index):
		return self.item[index]

# s = Stack()

# print(s.is_empty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# s.push(8.4)
# # print(s.peek())
# print(s.size())
# print(s.pop())
# print(s.pop())
# print(s.size())
# print(s.displayVal(0))