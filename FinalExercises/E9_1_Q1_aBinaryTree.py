class BinaryTree:

	def __init__(self,root):
		self.key = root
		self.leftChild = None
		self.rightChild = None

	def __repr__(self):
		return "Binary tree,key is " + self.key

	def insertLeft(self,newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			newTree = BinaryTree(newNode)
			newTree.leftChild = self.leftChild
			self.leftChild = newTree

	def insertRight(self,newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			newTree = BinaryTree(newNode)
			newTree.rightChild = self.rightChild
			self.rightChild = newTree

	def get_right_child(self):
		return self.rightChild

	def get_left_child(self):
		return self.leftChild

	def get_rootValue(self):
		return self.key

	def set_rootValue(self,value):
		self.key = value

	def search(self,value):
		if self!=None:
			if self.get_left_child()!=None:
				if self.get_left_child().search(value):
					return True

			if(self.get_rootValue()==value):
				return True

			if self.get_right_child()!=None:
				if self.get_right_child().search(value):
					return True

			return False

aBinaryTree  = BinaryTree("A")
aBinaryTree.insertLeft("B")
aBinaryTree.insertRight("C")

b = aBinaryTree.get_left_child()
b.insertLeft("D")
b.insertRight("E")

c = aBinaryTree.get_right_child()
c.insertLeft("F")
c.insertRight("G")

if aBinaryTree.search("A"):
	print("Found!!")
else:
	print("Not Found!!")