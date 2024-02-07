from BinaryTree import BinaryTree

def bfs_Search(Tree,value):
	thisLvl = [Tree]
	while thisLvl:
		nextLvl = []
		currentLvl = []
		for i in thisLvl:

			currentLvl.append(i.get_rootValue())

			if i.get_leftChild()!=None:
				nextLvl.append(i.get_leftChild())
			if i.get_rightChild()!=None:
				nextLvl.append(i.get_rightChild())

		if value in currentLvl:
			return True
		else:
			thisLvl = nextLvl

	return False



bTree = BinaryTree("A")

bTree.insert_left("B")
bTree.insert_right("C")

b = bTree.get_leftChild()
b.insert_left("D")
b.insert_right("E")

c= bTree.get_rightChild()
c.insert_left("F")
c.insert_right("G")

print(bfs_Search(bTree,"H"))
