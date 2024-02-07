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

	def inorder(self):
		if self!=None:
			if self.get_leftChild()!= None:
				self.get_leftChild().inorder()

			print(self.get_rootValue())

			if self.get_rightChild()!=None:
				self.get_rightChild().inorder()

	def preorder(self):
		if self!=None:
			
			print(self.get_rootValue())

			if self.get_leftChild()!=None:
				self.get_leftChild().preorder()

			if self.get_rightChild()!=None:
				self.get_rightChild().preorder()

	def postorder(self):
		if self!=None:
			if self.get_leftChild()!=None:
				self.get_leftChild().postorder()
			if self.get_rightChild()!=None:
				self.get_rightChild().postorder()
			print(self.get_rootValue())


	def bfs(self):
		this_level= [self]
		while this_level:
			next_level = []
			level = []
			for n in this_level:
				level.append(n.get_rootValue())

				if n.get_leftChild()!=None:
					next_level.append(n.get_leftChild())
				if n.get_rightChild()!=None:
					next_level.append(n.get_rightChild())
			print(",".join(level))
			this_level = next_level



root = BinaryTree("A")

root.insert_left("B")
root.insert_right("C")

b = root.get_leftChild()

b.insert_left("D")
b.insert_right("E")

d = b.get_leftChild()

d.insert_left("F")
d.insert_right("G")

# print("------------In Order--------------")
# root.inorder()
# print("------------Pre Order--------------")
# root.preorder()
# print("------------Post Order--------------")
# root.postorder()

root.bfs()

