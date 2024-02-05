class BinaryTree:

	def __repr__(self):
		return "Binary Tree,Key is " + self.key

	def __init__(self,root):
		self.key = root
		self.left_child = None
		self.right_child = None

	def insert_left(self,new_node):
		if self.left_child == None:
			print("New Node coming to 1st node!")
			self.left_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.left_child = self.left_child
			self.left_child = t

	def insert_right(self,new_node):
		if self.right_child ==None:
			self.right_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.right_child = self.right_child
			self.right_child = t

	def set_rootValue(self,obj):
		self.key = obj

	def get_rootValue(self):
		return self.key

	def get_leftChild(self):
		return self.left_child

	def get_rightChild(self):
		return self.right_child

	def postorder(self):
		if self!=None:
			if self.get_leftChild()!=None:
				self.get_leftChild().postorder()
			if self.get_rightChild()!=None:
				self.get_rightChild().postorder()
			print(self.get_rootValue())

