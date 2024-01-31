from node import Node

class OrderedList:
	def __init__(self):
		self.head = None

	def is_Empty(self):
		return self.head == None

	def size(self):
		count = 0
		current = self.head
		# while current.get_next()!=None:
		while current != None:
			count= count+1
			current = current.get_next()

		return count

	def search(self,item):
		current = self.head
		found = False
		# stop = False

		while current!=None :
			if current.get_data() == item:
				found = True
				break
			else:
				if current.get_data()>item:
					break
				else:
					current = current.get_next()
		return found

# Head->1->2->5->9->44->None

	def add(self,item):
		current = self.head
		previous = None

		while current!=None :
			if current.get_data() >= item:
				# print("Going to break!!")
				break
			# print("Moving to next room!")
			previous = current
			current = current.get_next()

		temp = Node(item)

		if previous==None:
			# print("First room!")
			temp.set_next(self.head)
			self.head = temp
		else:
			previous.set_next(temp)
			temp.set_next(current)

		print("Completely added ",item)

	def pop(self):
		current = self.head
		previous = None

		while current.get_next()!=None:
			previous = current
			current = current.get_next()

		previous.set_next(None)
		return current.get_data()

	def display(self):
		current = self.head
		print("The list is",end="")
		while current!=None:
			print(" ",current.get_data(),end="")
			current = current.get_next()
		print("")

	def remove(self,item):
		current = self.head
		previous = None
		found = False

		while current!=None:
			if item==current.get_data():
				found =True
				break
			else :
				previous = current
				current = current.get_next()
		if found:
			if previous==None:
				current.set_next(self.head)
			else:
				previous.set_next(current.get_next())
			print(item,"is removed from the list!")
		else:
			print("The input was not found in array!")

# Head->1->2->5->9->44->None

myList = OrderedList()

# print("Is my list is empty? ",myList.is_Empty())
myList.add(3)
myList.add(31)
myList.add(71)
myList.add(10)
myList.add(5)
myList.add(1)
print("Size of the list is",myList.size())
myList.display()
print("Now successfully popped",myList.pop())
print("Size of the list is",myList.size())
myList.display()
myList.remove(10)
print("Size of the list is",myList.size())
myList.display()
