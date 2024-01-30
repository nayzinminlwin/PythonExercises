from stack import Stack

def DeciToOct(num):
	try:
		s= Stack()
		num = int(num)
		octal =""

		while num>0:
			expo = num%8;
			s.push(expo)
			num = num // 8

		while not s.is_empty():
			octal = octal + str(s.pop())

		return octal

	except ValueError :
		print("Input numbers only!")

a = input("Enter a decimal number u want me to change to Octal :")
print(DeciToOct(a))