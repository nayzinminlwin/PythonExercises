# numberCount = int(input("Enter the number count :"))
# result = 1
# gg = 1
# print(result," ",end="")

# for x in range(1,numberCount):
# 	result = result + gg;
# 	gg = result
# 	print(result," ",end="")

a = 0
b = 1

n = int(input("Enter the number count :"))

if n<0:
	print("incorrect input")

elif n==0:
	print(a)

elif n==1:
	print(b)

else :
	print(b," ",end="")
	for x in range(1,n):
		c=a+b
		a=b
		b=c
		print(c," ",end="")
