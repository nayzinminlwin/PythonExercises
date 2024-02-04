def shellSort(array):
	gap = len(array)//2

	while gap>0:
		for i in range(gap,len(array)):
			val = array[i]
			j = i
			while j>=gap and array[j-gap]>val:
				array[j] = array[j-gap]
				j -=gap 
				# j = j - gap
			array[j] = val

		gap //=2
		# gap = gap//2
	return array


print(shellSort([5,6,4,7,12,9,1,8,32,49]))