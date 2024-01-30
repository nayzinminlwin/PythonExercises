a =  [3,4,1,3,9,7]
b = input("Enter a number u want to find :")
match = False
try:
	b = int(b)
	for x in range(len(a)):
		if a[x]==b:
			print("The input match a number in array at index :",x)
			match = True
		# 	break;
		# else :
		# 	# print("incoming!!!")
		# 	match = False

	if match == False :
		print("The input dont have any match in array.")

except ValueError :
	print("Enter integers only!")
	