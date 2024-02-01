def fibRecur(n):
	if n<2:
		return n
	else:
		return fibRecur(n-1)+fibRecur(n-2)

# print(fibRecur(10))


# n! = n*(n-1)!

def factorial(n):
	if n==1:
		return n
	else:
		result = n * int(factorial(n-1))
		print(result)
		return result

# print("Factorial of 4 is",factorial(4))

# A(m,n)=A(m−1,A(m,n−1))
def ackermann(a,b):
	if a==0:
		return b+1
	elif b==0:
		return ackermann(a-1,1)
	else:
		return ackermann(a-1,ackermann(a,b-1))

print("Ackermann of 2,5 is",ackermann(2,5))