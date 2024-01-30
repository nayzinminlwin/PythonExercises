# parChecker.py
from stack import Stack

def parChecker(symbolString):
	s = Stack()
	stackNotEmpt = True
	index = 0
	while index < len(symbolString) and stackNotEmpt:
		symbol = symbolString[index]
		if symbol == "(":
			s.push(symbol)
			print(index,"times pushing",symbol)
		else:
			if s.is_empty():
				print(index,"Returning false coz stack is empty!")
				stackNotEmpt = False
			else:
				s.pop()
				print(index,"times popping.")

		index = index + 1

	if stackNotEmpt and s.is_empty():
		return True
	else:
		return False

print(parChecker('()(g()'))
