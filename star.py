count = input("How many stars do u want ? :")

try:
	count = int(count)

	for x in range(1,count+1):
		for y in range(x):
			print("*",end="")
		print(end="\n")

except ValueError:
	print("Enter number only!")

