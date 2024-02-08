import time

def sum_of_num(n):
	start = time.time()
	total = 0;
	for x in range(1,n+1):
		total = total+x
	end = time.time()

	return total,end-start

def math_Sum_of_num(n):
	start = time.time()
	total = n*(n+1)/2
	end = time.time()
	return total,end-start

# print(sum_of_num(99999999))
for i in range(5):
	print("Sum is %d , %.7f seconds." % sum_of_num(9999999))

print('=======================================')

for i in range(5):
	print("Sum is %d , %.7f seconds." % math_Sum_of_num(9999999))
