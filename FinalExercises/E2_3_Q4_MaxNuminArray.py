anArray = [1255,2125,1050,2506,1236,1048,2010,5055]

maxNum = anArray[0]
maxRoom = 0
for x in range(len(anArray)):
	if maxNum<anArray[x]:
		maxNum = anArray[x]
		maxRoom = x

print("Maximum number in array is",maxNum,"and found at room",maxRoom)