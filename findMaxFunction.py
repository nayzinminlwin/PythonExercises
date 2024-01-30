listA = [1048,1255,2125,1050,2506,1236,2010,1055]
listB = [1048,5477,2125,1050,2506,1236,2010,1055]

def maxFun(arr):

	max = arr[0]

	for x in arr:
		if x>max:
			max = x;

	return max

print("The maximun num in array is",maxFun(listA))
print("The maximun num in array is",maxFun(listB))