def fiboLoop(num):
	a = 0
	b = a+1
	print(a,"",b," ",end="")
	for x in range(1,num):
		c = a+b;
		a=b;
		b=c;
		print(c," ",end="")

fiboLoop(10)
