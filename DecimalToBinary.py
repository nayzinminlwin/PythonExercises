from stack import Stack


def divideBy2(num):

	s = Stack()
	binaryy = ""
	try:
		num = int(num)

		while num > 0:

			mod=num%2
			s.push(mod)
			print("Divided and pushed!",mod)

			num = num//2

		# if not s.is_empty():

		# 	for x in reversed(range(len(s.item))):
		# 		binaryy = binaryy + str(s.item[x])

		# 	return binaryy	

		while not s.is_empty():
			binaryy = binaryy + str(s.pop())

		return binaryy
	
	except ValueError:
		print("Input numbers only!")


a = input("Enter a number u want to change to binary :")
print(divideBy2(a))