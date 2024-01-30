# parChecker.py
from stack import Stack
def parChecker(symbolString):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbolString) and balanced:
		print("Incoming into the loop",index)
		symbol = symbolString[index]

		s.push(symbol)

		if symbol == "(":
			print("i see a ( here!")
			s.push(")")
			print("i push ).")
		else:
			if s.is_empty():
				print("stack is empty")
				balanced = False
			else:
				print("i see a ) here!")
				print("now i pop {}.".format(s.peek()))
				s.pop()

		index = index + 1
	
	print("---------------------------------")	
	if balanced and s.is_empty():
		print("Balanced & Empty! Gonna print the array",s.is_empty())
		return True
	else:
		print("Array size is",s.size())
		print("Gonna print the array")
		for x in range(s.size()):
			# print(x,"Values:",s.item[x])
			print(s.item[x],end="")

		return "\nhehe"


print(parChecker('((()()()))'))