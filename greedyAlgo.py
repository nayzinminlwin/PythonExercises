def quickSorting(anArray):
	if len(anArray)<2:
		return anArray
	else:
		pivot = [anArray[len(anArray)//2]]
		left = [x for x in anArray if x<pivot[0]]
		right = [x for x in anArray if x>pivot[0]]

		return quickSorting(left)+pivot+quickSorting(right)


def greedyAlgo(array_a,mani):
	sortedArray = quickSorting(array_a)

	while mani>=sortedArray[0]:
		print("While loop entry coz",mani,">=",sortedArray[0])

		for x in range(len(sortedArray)-1,-1,-1):
			# print("Incoming into for loop with ",x)

			if mani >= sortedArray[x]:
				print(mani,">=",sortedArray[x])

				print("now gonna substract",sortedArray[x])
				mani = mani - sortedArray[x]

				print("Now mani is",mani)
				break

	return mani

MMK = [10000,5000,1000,500,200,100,50]
print(greedyAlgo(MMK,20655))