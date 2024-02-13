n = int(input("Enter a number for fibo sequence:"))
a = 1
b,c = 0,0;

for x in range(n):
	c = a+b
	print(c)
	a=b
	b=c