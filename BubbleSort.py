# def bubbleSort(array):
# 	for num in range(len(array)-1,0,-1):
# 		for x in range(num):
# 			if array[x]>array[x+1]:
# 				temp = array[x]
# 				array[x] = array[x+1]
# 				array[x+1]= temp
# 	return array

#we saw the array is being sorted even it is sorted already
#so we write an efficient code by checking if it is already sorted or not.

def bubbleSort(array):
	size = len(array)-1
	exchange = True

	while size>0 and exchange:
		exchange = False

		for i in range(size):
			if array[i]>array[i+1]:
				exchange = True
				temp = array[i]
				array[i] = array[i+1]
				array[i+1]= temp

		size = size-1
	return array

print(bubbleSort([1,6,4,7,8,9]))