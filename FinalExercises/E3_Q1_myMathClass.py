class myMath:
	def __init__(self):
		return None

	def mathPlus(self,a,b):
		return a+b

	def mathMinus(self,a,b):
		return a-b

	def mathMultiply(self,a,b):
		return a*b

	def mathDivide(self,a,b):
		if b==0:
			return "Can't be devided by Zero!"
		else:
			return a/b

aCalc = myMath()
print(aCalc.mathPlus(1,2))
print(aCalc.mathDivide(1,0))