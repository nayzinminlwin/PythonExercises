def mergeSorting(left,right):
	leftIndex = 0;
	rightIndex = 0;
	resultArray = []

	while leftIndex<len(left) and rightIndex<len(right):

		if left[leftIndex]<right[rightIndex]:
			resultArray.append(left[leftIndex])
			leftIndex+=1
		else:
			resultArray.append(right[rightIndex])
			rightIndex+=1

	if leftIndex<len(left):
		resultArray.extend(left[leftIndex:])
	if rightIndex<len(right):
		resultArray.extend(right[rightIndex:])

	return resultArray

def MergeSortExe(anArray):
	if len(anArray)<2:
		return anArray
	else:
		mid = len(anArray)//2
		# print(anArray[:mid],anArray[mid:])
		return mergeSorting(MergeSortExe(anArray[:mid]),MergeSortExe(anArray[mid:]))

testingArray = [84,58,53,87,68]
print(MergeSortExe(testingArray))
