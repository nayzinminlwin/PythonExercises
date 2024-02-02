def recurBinarySearch(array,val):

	if len(array) == 0:
		return False


	mid =len(array)//2
	midVal = array[mid]
	if midVal == val:
		return True
	else:
		if val < midVal:
			return recurBinarySearch(array[:mid],val)
		else:
			return recurBinarySearch(array[mid+1:],val)

print(recurBinarySearch([8,14,18,20,26,66,78],18))
print(recurBinarySearch([8,14,18,20,26,66,78],19))