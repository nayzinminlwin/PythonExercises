def divideBy16(aDeciNum):
	resultArr = []
	exponent = aDeciNum
	reminder = None

	while exponent>=1:
		reminder = exponent%16
		exponent = exponent//16
		if reminder<10:
			resultArr.insert(0,reminder)
		elif reminder==10:
			resultArr.insert(0,"A")
		elif reminder==11:
			resultArr.insert(0,"B")
		elif reminder==12:
			resultArr.insert(0,"C")
		elif reminder==13:
			resultArr.insert(0,"D")
		elif reminder==14:
			resultArr.insert(0,"E")
		elif reminder==15:
			resultArr.insert(0,"F")
		else:
			resultArr.insert(0,"Hehehe")

	return resultArr

print("".join(map(str,divideBy16(668))))
