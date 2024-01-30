num1 = input("Enter 1st number :")
op = input("Enter Operator(+,-,*,/) :")
num2 = input("Enter 2nd number :")
Output = True

try:
	num1 = int(num1)
	num2 = int(num2)

	if op == "+":
		result = num1+num2
	elif op == "-":
		result = num1-num2
	elif op == "*":
		result = num1*num2
	elif op == "/":
		try:
			result = num1/num2
		except ZeroDivisionError :
			Output = False
			print("Cant be divided by Zero.")
	else :
		Output = False
		print("Wrong Operator")

	if Output :
		print("Result is",result)


	
except ValueError :
	print("Input must be numbers only.")
	print(ValueError)