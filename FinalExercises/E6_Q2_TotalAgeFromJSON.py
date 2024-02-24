room = [{'Name': 'Aung Ko', 'Age': 7, 'Gender' : 'male'}, 
{'Name': 'Ko Ko', 'Age': 8, 'Gender' : 'male'},
{'Name': 'Aye Aye', 'Age': 7, 'Gender' : 'female'},
{'Name': 'Htet Htet', 'Age': 8, 'Gender' : 'female'},
{'Name': 'Win Aung', 'Age': 7, 'Gender' : 'male'}]

totalAge = 0;
for x in room:
	totalAge = totalAge + x["Age"]

print("Total age is ",totalAge)