class Node:

	def __init__(self,value):
		self.value = value
		self.child = []

	def __repr__(self):
		return "Value is " + self.value

	def insert_child(self,node):
		self.child.append(node)

	def get_child(self):
		return self.child

	def nodeBFS(self):
		thisLvl = [self]
		while thisLvl:
			nextLvl = []
			currentLvl = []
			for x in thisLvl:
				currentLvl.append(x.value)

				if len(x.child)>0:
					nextLvl = nextLvl + x.child

			if len(currentLvl)>0:
				print(",".join(currentLvl))

			thisLvl = nextLvl

	def preOrder(self):

		if self!=None:
			print(self.value)

			if self.child!=None:
				for x in self.child:
					x.preOrder()

	def postOrder(self):
		if self!=None:
			if self.child!=None:
				for x in self.child:
					x.postOrder()
			print(self.value)
				


root = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

root.insert_child(b)
root.insert_child(c)
root.insert_child(d)

e = Node("E")
f = Node("F")
g = Node("G")

b.insert_child(e)
b.insert_child(f)
b.insert_child(g)

h = Node("H")
i = Node("I")

c.insert_child(h)
c.insert_child(i)

j = Node("J")
d.insert_child(j)

# print(root.value)
# print(root.child)
# print(root.child[0].value)
# print(root.child[0].child)
# print(root.child[0].child[1].value)

# print(root)
# for x in root.child:
# 	print(x)
# 	for y in x.child:
# 		print(y)

# root.nodeBFS()
root.preOrder()
root.postOrder()