def noteChange(cash):
	
	notes = [25,50,100,200,500,1000,5000,10000]
	count = []

	while cash>=25:
		for x in range(len(notes)-1,-1,-1):

			if cash>=notes[x]:
				cash = cash - notes[x]

				if notes[x] == 25:
					count.append("Candy")
				else:
					count.append(notes[x])

				break

	print("Ramaining cash is",cash)
	# print(count)

	gg = 1;
	for x in range(len(count)):
		# print("x is ",x)

		if x==len(count)-1:
			print("You gotta give",count[x],"x",gg)
			break

		if count[x] == count[x+1]:
			gg = gg +1;
		else:
			print("You gotta give",count[x],"MMK x",gg)
			gg = 1;

c = input("How much cash u want to pay : ")
noteChange(int(c))