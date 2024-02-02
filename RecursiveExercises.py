def fibRecur(n):
	if n<2:
		return n
	else:
		return fibRecur(n-1)+fibRecur(n-2)

# print(fibRecur(10))


# n! = n*(n-1)!
def factorial(n):
	if n==0:
		return 1
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

# print("Ackermann of 2,5 is",ackermann(2,5))

#T(n) = 2 x T(n-1) + 1
def towersOfHanoi(n):
	if n==1:
		return n;
	else :
		return (2*towersOfHanoi(n-1))+1

print("Towers of Hanoi of 5 is",towersOfHanoi(5))

# C(n,k)=C(n-1,k-1)+C(n-1,k)
def binomialCoefficient(n,k):
	if k==0 or n==0 or n==k:
		return 1
	else:
		return (binomialCoefficient(n-1,k-1))+(binomialCoefficient(n-1,k))

print("Binomial Coefficient of 5,11 is",binomialCoefficient(10,7))
		
