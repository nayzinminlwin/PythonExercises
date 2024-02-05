from BinaryTree import BinaryTree

root = BinaryTree('a')

print(root)

print(root.get_leftChild())
print(root.get_rightChild())

root.insert_left('b')
print(root.get_leftChild().get_rootValue())

root.insert_right('c')
print(root.get_rightChild().get_rootValue())

root.get_rightChild().set_rootValue("Hello")
print(root.get_rightChild().get_rootValue())

root.insert_left('d')
print(root.get_leftChild().get_rootValue())
print(root.get_leftChild().get_leftChild().get_rootValue())