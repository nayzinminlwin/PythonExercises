from node import Node

class OrderedList:
	def __init__(self):
		self.head = None

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
				print("Going to break!!")
				break
			print("Doing the two lines under!")
			previous = current
			current = current.get_next()

		temp = Node(item)

		if previous==None:
			print("First room!")
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

myList = OrderedList()

# print("Is my list is empty? ",myList.is_Empty())
myList.add(3)
myList.add(31)
myList.add(71)
myList.add(10)
myList.add(5)
myList.add(1)
print("Now successfully popped",myList.pop())


