class myMath:

	def __init__(self):

		pass

	def add(self,a,b):
		return a+b

	def minus(self,a,b):
		return a-b

	def multiply(self,a,b):
		return a*b

	def divide(self,a,b):
		if b!=0 :
			return a/b
		else :
			print("Cant be divided by zero.")

	def power(self,a,b):
		multiplier = a
		for x in range(b-1):
			a = a*multiplier
			
		return a


aCalculator = myMath()
num1 = input("Input first num :")
sign = input("Input Sign :")
num2 = input("Input second num :")

try:
	num1 =int(num1)
	num2 = int(num2)

	if sign == "+" :
		print("The addition of two numbers is ",aCalculator.add(num1,num2))
	elif sign == "-" :
		print("The substration of two numbers is ",aCalculator.minus(num1,num2))
	elif sign == "*" :
		print("The multiplication of two numbers is ",aCalculator.multiply(num1,num2))
	elif sign == "/" :
		print("The division of two numbers is ",aCalculator.divide(num1,num2))
	elif sign == "^" :
		print("The power of two numbers is ",aCalculator.power(num1,num2))
	else : 
		print("Invalid sign!!")

except ValueError :
	print("Input numbers only!")


