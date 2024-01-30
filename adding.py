x = input("Enter x :")
y = input("Enter y :")

try:
	x = int(x)
	y = int(y)
	print ("X + Y =", x+y)

except ValueError :
	print("Please enter number only!")
