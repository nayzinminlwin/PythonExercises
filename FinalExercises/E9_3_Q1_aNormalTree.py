class Node:
	def __init__(self,root):
		self.key = root
		self.child = []

	def get_rootValue(self):
		return str(self.key)

	def addChild(self,name):
		newChild = Node(name)
		self.child.append(newChild)

	def getChild(self):
		return self.child

not_Bi_Tree = Node("A")

b = Node("B")
c = Node("C")
d = Node("D")

print(d.get_rootValue())

not_Bi_Tree.addChild(b)
not_Bi_Tree.addChild(c)
not_Bi_Tree.addChild(d)

e= Node("E")
f = Node("F")
g = Node("G")

b.addChild(e)
b.addChild(f)
b.addChild(g)

for x in not_Bi_Tree.child:
	print(x.get_rootValue())
	# print(x)