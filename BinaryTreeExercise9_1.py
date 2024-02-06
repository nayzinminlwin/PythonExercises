from BinaryTree import BinaryTree
import site
import sys

def BinaryTreeSearch(Tree,Val):

	if Tree!=None and Val!=None:
		print("Both not non.So incoming!")
		found = None
		currentVal = Tree.get_rootValue()
		aString = str(currentVal)

		if aString==str(Val):
			print("Found!!")
			found = True

		if found:
			return found
			# exit()
			sys.exit("Found!")
		else:
			if Tree.get_leftChild()!=None:
				BinaryTreeSearch(Tree.get_leftChild(),Val)
			if Tree.get_rightChild()!=None:
				BinaryTreeSearch(Tree.get_rightChild(),Val)

	return found

aTree = BinaryTree("A")
aTree.insert_left("B")
aTree.insert_right("C")
b = aTree.get_leftChild()
c = aTree.get_rightChild()
b.insert_left("D")
b.insert_right("E")
c.insert_left("F")
c.insert_right("G")
aTree.postorder()

print(BinaryTreeSearch(aTree,"G"))