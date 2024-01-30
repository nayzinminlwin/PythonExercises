from node import Node

class UnorderedList:
	def __init__(self):
		self.head = None

	def is_Empty(self):
		return self.head == None

	def add(self,Val):
		temp = Node(Val)
		temp.set_next(self.head)
		self.head = temp

	def listSize(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.get_next()
		return count

myList = UnorderedList()
print(myList.is_Empty())
myList.add(3)
myList.add(31)
myList.add(71)
myList.add(10)
myList.add(5)
myList.add(1)
print(myList.is_Empty())
print("Size of the list is",myList.listSize())