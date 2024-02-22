from E3_Q1_myMathClass import myMath

class myMathExt(myMath):
	def __init__(self):
		return None

	def mathSquare(self,a):
		return a*a;

	def mathTube(self,a):
		return a*a*a;

	def mathPower(self,a,b):
		result = 1
		for x in range(b):
			result = result*a;
		return result;

secondCalc = myMathExt()
print("3 plus 3 is ",secondCalc.mathPlus(3,3))
print("3 divide 3 is ",int(secondCalc.mathDivide(3,3)))
print("3 square is",secondCalc.mathSquare(3))
print("3 tube is",secondCalc.mathTube(3))
print("3 power 8 is",secondCalc.mathPower(3,8))