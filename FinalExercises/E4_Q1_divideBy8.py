def divideBy8(BinaryNum):
	result = []
	reminder = 0
	exponent = BinaryNum

	while exponent>1:
		reminder = int(exponent%8)
		exponent = exponent/8;
		# print("Now i is",i)
		# result[i] = reminder
		result.insert(0,reminder)
	return result

print(divideBy8(554))
print(''.join(map(str,divideBy8(554))))