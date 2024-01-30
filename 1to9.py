x = input("Enter a number from 0 to 9:")

try:
	x = int(x)
	while (x>9 or x<0):
		x = int(input("Number must be from 0 to 9:"))

	print("You entered",x)


except ValueError:
	print("Input must be numbers only!")

