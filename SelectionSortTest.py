def selectionSortTest(array):

	for x in range(len(array)):
		pos_of_min = x

		for y in range(x,len(array)):
			if array[y]<array[pos_of_min]:
				pos_of_min = y;

		temp = array[x]
		array[x]=array[pos_of_min]
		array[pos_of_min]=temp
		
	return array

test = [5,6,4,7,12,9]
print(selectionSortTest(test))