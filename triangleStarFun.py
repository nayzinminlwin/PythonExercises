# def minus(a,b):
# 	return a-b

# c = int(input("num1 :"))
# d = int(input("num2 :"))

# print("Distraction of the two num is",minus(c,d))

def triangle_Star(starCount):
	try:
		starCount = int(starCount)
		for x in range(starCount+1):
			for y in range(x):
				print("*",end="")
			print("")

	except ValueError:
		print("Enter Numbers only!")
		

userInput = input("How many lines of star u want :")
triangle_Star(userInput)


