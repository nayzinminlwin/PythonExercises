def arraySplit(anArray):
	if len(anArray)<2:
		return anArray
	else :
		mid = len(anArray)//2
		print("Mid index is",mid)
		print("1st part is ",anArray[:mid])
		print("2nd part is ",anArray[mid:])

gg = [7,8,9,6,5]
arraySplit(gg)