def sequentialSearch(array,val):
	for (index,value) in enumerate(array):
		if val == value:
			return index
	return -1

numbers = [1,2,3,4,5,6,9]

res = sequentialSearch(numbers,5)

if res != -1:
	print("Found at",res)
else:
	print("404,Not Found!")