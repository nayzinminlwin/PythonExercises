anArray = [3,4,1,2,9,7]

cusNum = int(input("What num u want to find:"))
fIndex = None
for x in range(len(anArray)):
	if cusNum == anArray[x]:
		fIndex = x;
		break

if fIndex!=None:
	print("Found at :",fIndex)
else:
	print("Not Found!")