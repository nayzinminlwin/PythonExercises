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

	def display(self):
		current = self.head
		print("The UnorderedList is ",end="")
		while current != None: 
			print(current.get_data()," ",end="")
			current = current.get_next()
		print("")

	def search(self,val):
		found = False
		current = self.head
		while current != None and not found:
			if val == current.get_data():
				found = True
			else:
				current = current.get_next()
	
		return found

	def index(self,item):
		indexNum = -1
		current = self.head
		while current != None:
			indexNum = indexNum + 1
			if item == current.get_data():
				break
			else :
				current = current.get_next()

		return indexNum

	def pop(self):
		current = self.head
		previous = None

		while current!= None :
			previous = current
			current = current.get_next()
			# print("Now i am at",self.index(current.get_data()))
			# print("previous data is at",self.index(previous.get_data()))

		# previous.set_next(None)
		# previous.head = None
		# previous.set_next(current)
		# self.delete(previous.get_data())
		if previous == None :
			self.head = current.get_next()
		else: 
			previous.set_next(None)


	def delete(self,val):

		current = self.head
		previous = None
		found = False

		while current!= None and not found:
			if val == current.get_data():
				found = True
			else:
				previous = current
				current = current.get_next()

		if found:
			if previous == None :
				self.head = current.get_next()
			else: 
				previous.set_next(current.get_next())

 # append,insert,pop

myList = UnorderedList()
# print(myList.is_Empty())
myList.add(3)
myList.add(31)
myList.add(71)
myList.add(10)
myList.add(5)
myList.add(1)
# print(myList.is_Empty())
# print("The index of the value is",myList.index(31))
# print("Size of the list is",myList.listSize())
# print(myList.search(10))
# myList.delete(10)
print("Size of the list is",myList.listSize())
myList.display()
myList.pop()
print("Size of the list is",myList.listSize())
myList.display()