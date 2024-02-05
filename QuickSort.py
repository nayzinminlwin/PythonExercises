def quickSort(array):

	less = []
	more = []
	pivotList = []

	if len(array)<=1:
		return array
	else:
		pivot = array[0]
		for i in array:
			if i<pivot:
				less.append(i)
			elif i>pivot:
				more.append(i)
			else:
				pivotList.append(i)

		less = quickSort(less)
		more = quickSort(more)

		return less+pivotList+more

qs = [4,7,8,1,-6,3,2]
print(quickSort(qs))