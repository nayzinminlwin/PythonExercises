class Node:
	def __init__(self,root):
		self.key = root
		self.child = []

	def get_rootValue(self):
		return self.key

	def addChild(self,node):
		self.child.append(node)

	def getChild(self):
		return self.child

	def postOrder(self):
		# print("Welcome to Preorder Method!")
		if self!=None:
			if(len(self.child)>0):
				# for child in self.getChild():
				# 	child.get_rootValue().postOrder()
				for child in reversed(self.getChild()):
					child.postOrder()

			print(self.key)

	def preOrder(self):
		if self!=None:
			print(self.key)
			if(len(self.child)>0):
				for child in self.getChild():
					child.preOrder()


not_Bi_Tree = Node("A")

b = Node("B")
c = Node("C")
d = Node("D")

not_Bi_Tree.addChild(b)
not_Bi_Tree.addChild(c)
not_Bi_Tree.addChild(d)

# print(d.get_rootValue())
# for x in not_Bi_Tree.child:
# 	print(x.get_rootValue().get_rootValue())
# 	# print(x)

e= Node("E")
f = Node("F")
g = Node("G")

b.addChild(e)
b.addChild(f)
b.addChild(g)

h = Node("H")
i = Node("I")

c.addChild(h)
c.addChild(i)

j = Node("J")
d.addChild(j)

print("===========PostOrder===========")
not_Bi_Tree.postOrder()
print("==========PreOrder===========")
not_Bi_Tree.preOrder()