n = int(input("For how many number u wanna know even and odd:"))

for x in range(n):
	if x==0:
		print(x,"Even")
	elif x%2==0:
		print(x,"Even")
	else:
		print(x,"Odd")
