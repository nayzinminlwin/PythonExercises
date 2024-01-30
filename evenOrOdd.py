count = int(input("How many numbers u wanna know :"))

for x in range(1,count+1):
	if x%2 == 0:
		print(x,"is even.")
	else:
		print(x,"is odd.")