def binarySearch(array,val):
	first = 0
	last = len(array)-1
	
	found = False

	while first <= last and not found:
		mid = (first+last)//2
		midVal = array[mid]

		if val == midVal:
			found = True
			return found
		else:
			if val < midVal :
				last = mid-1
			else :
				first = mid+1
	return found

numbers=[1,2,2,3,4,5,6,7,7,7,9]
print(binarySearch(numbers,10))

