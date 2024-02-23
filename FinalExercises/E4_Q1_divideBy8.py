class Stack:
	def __init__(self):
		self.item = []

	def isEmpty(self):
		return self.item == []

	def push(self,newItem):
		self.item.append(newItem)

	def pop(self):
		return self.item.pop()

	def peek(self):
		return self.item[len(self.item)-1]

	def size(self):
		return len(self.item)

def divideBy8(BinaryNum):
	result = Stack()
	reminder = 0
	exponent = BinaryNum

	while exponent>1:
		reminder = int(exponent%8)
		exponent = exponent/8;
		# result[i] = reminder
		# result.insert(0,reminder)
		result.push(reminder)
	resultString = ""
	while not result.isEmpty():
		resultString = resultString + str(result.pop())
	return resultString

print(divideBy8(554))
# print(''.join(map(str,divideBy8(554))))