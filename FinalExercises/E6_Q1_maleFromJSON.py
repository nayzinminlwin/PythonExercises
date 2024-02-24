room = [{'Name': 'Aung Ko', 'Age': 7, 'Gender' : 'male'}, 
{'Name': 'Ko Ko', 'Age': 8, 'Gender' : 'male'},
{'Name': 'Aye Aye', 'Age': 7, 'Gender' : 'female'},
{'Name': 'Htet Htet', 'Age': 8, 'Gender' : 'female'},
{'Name': 'Win Aung', 'Age': 7, 'Gender' : 'male'}]

# print(room[0]["Gender"])
for x in room:
	if x["Gender"] != "male":
		print(x["Name"])