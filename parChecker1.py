from stack import Stack
def parChecker1(symbolString):
	s = Stack()
	stackNotEmpt = True
	index = 0
	while index < len(symbolString) and stackNotEmpt:
		symbol = symbolString[index]
		if symbol in "([{":
			s.push(symbol)
			print(index,"times pushing",symbol)
		else:
			if s.is_empty():
				print(index,"Returning false coz stack is empty!")
				stackNotEmpt = False
			else:
				top = s.pop()
				print(index,"times popping.")
				print(top,symbol)

				if not matches(top,symbol):
					print(index,"Open & Close dont match.")
					stackNotEmpt = False

		index = index + 1
		print("----------------------------")
	print("======================================================")

	if stackNotEmpt and s.is_empty():
		return True
	else:
		return False

def matches(a,b):
	opens = "([{"
	closers = ")]}"
	# print(a,b)
	# print("Opener is",opens.index(a))
	# print("Closer is",closers.index(b))
	return opens.index(a) == closers.index(b)

print(parChecker1('{{([][])}()}'))
print(parChecker1('[{()]'))
# print(parChecker1('(})(((((()'))
