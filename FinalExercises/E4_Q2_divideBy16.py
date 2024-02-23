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


def divideBy16(aDeciNum):
	resultArr = Stack()
	exponent = aDeciNum
	reminder = None

	while exponent>=1:
		reminder = exponent%16
		exponent = exponent//16
		if reminder<10:
			# resultArr.insert(0,reminder)
			resultArr.push(reminder)
		elif reminder==10:
			# resultArr.insert(0,"A")
			resultArr.push("A")
		elif reminder==11:
			# resultArr.insert(0,"B")
			resultArr.push("B")
		elif reminder==12:
			# resultArr.insert(0,"C")
			resultArr.push("C")
		elif reminder==13:
			# resultArr.insert(0,"D")
			resultArr.push("D")
		elif reminder==14:
			# resultArr.insert(0,"E")
			resultArr.push("E")
		elif reminder==15:
			# resultArr.insert(0,"F")
			resultArr.push("F")
		else:
			# resultArr.insert(0,"Hehehe")
			resultArr.push("Hehehe")

	resultString = ""
	while not resultArr.isEmpty():
		resultString = resultString + str(resultArr.pop())
	return resultString

# print("".join(map(str,divideBy16(668))))
print(divideBy16(668))
