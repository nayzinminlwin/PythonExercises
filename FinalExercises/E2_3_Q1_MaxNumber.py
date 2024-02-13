anArray = [4456,1255,2125,1050,2506,1236,1048,2010,1055,3354]

maxNum = anArray[0];

for x in range(len(anArray)):
	if anArray[x]>maxNum:
		maxNum = anArray[x]
		
print("Max number is",maxNum)