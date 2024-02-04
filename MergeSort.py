def mergeSort(array):
	if len(array)<2:
		return array
	else:
		mid = len(array)//2
		return merge(mergeSort(array[:mid]),mergeSort(array[mid:]))

def merge(left,right):
	result = []
	left_idx,right_idx = 0,0;

	while left_idx < len(left) and right_idx < len(right):
		if left[left_idx]<=right[right_idx]:
			result.append(left[left_idx])
			left_idx+=1
		else:
			result.append(right[right_idx])
			right_idx+=1

	if left_idx < len(left):
		result.extend(left[left_idx:])
	if right_idx < len(right):
		result.extend(right[right_idx:])

	return result


print(mergeSort([4,5,1,3,9,7,2,10]))

