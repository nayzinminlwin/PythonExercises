from node import Node

# Head->1->99->66->None

class UnorderedList:
	def __init__(self):
		self.head = None

	def is_Empty(self):
		return self.head == None

	def add(self,Val):
		temp = Node(Val)
		temp.set_next(self.head)
		self.head = temp
		print("Added",Val)

	def insert(self,pos,Val):

		temp = Node(Val)
		current = self.head
		previous = None

		for x in range(pos):
			previous = current
			current = current.get_next()

		temp.set_next(current)
		previous.set_next(temp)
		print("Completely inserted",Val,"into index :",pos)

	def append(self,Val):
		temp = Node(Val)
		current = self.head

		while current != None:
			# print("Incoming into while!")
			if current.get_next() == None:
				# print("Finally into if clause")
				current.set_next(temp)
				temp.set_next(None)
				break

			else:
				current = current.get_next()
		print("Successfully appened",Val)

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

		if current!= None :
			count = self.listSize()

			for x in range(count-1):
				previous = current
				current = current.get_next()
				# print("Now i am at",self.index(current.get_data()))
				# print("previous data is at",self.index(previous.get_data()))
	
		# Head->1->99->66->None
		# print("current head is",current.get_data())
		# print("previous head is ",previous.get_data())
		previous.set_next(None)
		print("Successfully popped the last data from list.")

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

		print("Successfully deleted",val,"from the list.")


myList = UnorderedList()

print("Is my list is empty? ",myList.is_Empty())
myList.add(3)
myList.add(31)
myList.add(71)
myList.add(10)
myList.add(5)
myList.add(1)

myList.display()
print("The index of the value is",myList.index(31))

print("Is my data is in the list? ",myList.search(71))
myList.delete(71)
print("Is my data is in the list? ",myList.search(71))

myList.insert(2,99)
print("Size of the list is now",myList.listSize())
myList.display()
myList.pop()
print("Size of the list is now",myList.listSize())
myList.display()
myList.append(77)
print("Size of the list is now",myList.listSize())
myList.display()