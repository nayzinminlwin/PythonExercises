class anotherBinaryTree:

	def __init__(self,root):
		self.key = root
		self.leftChild = None
		self.rightChild = None

	def set_left_child(self,val):
		atree = anotherBinaryTree(val)
		if self.leftChild ==None:
			self.leftChild = atree;
		else:
			atree.leftChild = self.leftChild
			self.leftChild = atree

	def get_left_child(self):
		return self.leftChild

	def set_right_child(self,val):
		atree = anotherBinaryTree(val)
		if self.rightChild==None:
			self.rightChild = atree
		else:
			atree.rightChild = self.rightChild
			self.rightChild = atree

	def get_right_child(self):
		return self.rightChild

	def get_rootValue(self):
		return self.key

	def set_rootValue(self,val):
		self.key = val

	def search(self,searchValue):
		thisLevel = [self]
		while thisLevel:
			nextLevel = []
			currentLevel = []
			for n in thisLevel:
				if (n.get_rootValue()==searchValue):
					return True;

				currentLevel.append(n.get_rootValue())

				if n.get_left_child()!=None:
					nextLevel.append(n.get_left_child())
				if n.get_right_child()!=None:
					nextLevel.append(n.get_right_child())
			thisLevel = nextLevel
		return False

root = anotherBinaryTree("A")

root.set_left_child("B")
root.set_right_child("C")

b = root.get_left_child()

b.set_left_child("D") 
b.set_right_child("E")

c = root.get_right_child()

c.set_left_child("F")
c.set_right_child("G")

found = root.search("GG")
if found:
	print("Found")
else:
	print("Not Found!")