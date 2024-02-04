def mergeSort(array):
	if len(array)<2:
		return array
	else:
		mid = len(array)//2
		return merge(mergeSort(array[:mid]),mergeSort(array[mid:]))

def merge(left,right):
	result = []
	