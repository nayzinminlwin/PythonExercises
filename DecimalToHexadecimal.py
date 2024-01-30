from stack import Stack

def DecToHexa(num):
	s = Stack()
	hexaa = ""
	try:
		num = int(num)
		while num>0:
			expo = num%16

			if expo<10 :
				s.push(expo)
			elif expo == 10:
				s.push("A")
			elif expo == 11:
				s.push("B")
			elif expo == 12:
				s.push("C")
			elif expo == 13:
				s.push("D")
			elif expo == 14:
				s.push("E")
			elif expo == 15:
				s.push("F")
			else :
				s.push("GGWP")

			num = num //16

		while not s.is_empty():
			hexaa = hexaa + str(s.pop())

		return hexaa

	except ValueError:
		print("Enter numbers only!")

a = input("Enter a decimal number u transfer into HexaDecimal :")
print(DecToHexa(a))
