def listSum(numList):
	if len(numList)==1:
		return numList[0]
	else:
		return numList[0]+listSum(numList[1:])

print(listSum([1,2,5,9,7]))