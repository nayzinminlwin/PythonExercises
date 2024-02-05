from BinaryTree import BinaryTree
from stack import Stack

def build_parse_tree(theEquation):

	equationList = theEquation.split()
	p_stack = Stack()
	e_tree = BinaryTree('')
	p_stack.push(e_tree)
	current_tree = e_tree

	print(equationList)

	for i in equationList:
		print(i)
		print("Incoming!!")
		if i == '(':
			print("i see a (")
			current_tree.insert_left('')
			p_stack.push(current_tree)
			current_tree = current_tree.get_leftChild()

		elif i not in ['+','-','*','/',')']:
			print("i think this is integer")
			current_tree.set_rootValue(int(i))
			parent = p_stack.pop()
			print("Successfully popped!!!")
			current_tree = parent

		elif i in ['+','-','*','/']:
			print("i see an operator")
			current_tree.set_rootValue(i)
			current_tree.insert_right('')
			p_stack.push(current_tree)
			current_tree = current_tree.get_rightChild()

		elif i == ')':
			print("i see a )")
			parent = p_stack.pop()
			current_tree = parent

		else:
			print("i see nth.")
			raise ValueError

	return e_tree

# pt = build_parse_tree("((9+4)*(6-2))")

pt = build_parse_tree("( ( 9 + 4 ) * ( 6 - 2 ) )")
pt.postorder()