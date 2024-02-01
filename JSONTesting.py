import json

json_data = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

simple_dict = json.loads(json_data)

print(simple_dict['c'])

print(json.dumps(simple_dict))

room = [
 			{'Name': 'Aung Ko', 'Age': 7, 'Gender' : 'male'}, 
 			{'Name': 'Ko Ko', 'Age': 8, 'Gender' : 'male'},
			{'Name': 'Aye Aye', 'Age': 7, 'Gender' : 'female'},
			{'Name': 'Htet Htet', 'Age': 8, 'Gender' : 'female'},
			{'Name': 'Win Aung', 'Age': 7, 'Gender' : 'male'}
		]

for x in room:
	if str(x["Gender"])=="male":
		print(x['Name'])

total_age = 0
for y in room:
	total_age = total_age + int(y["Age"])

print(total_age)


