dict = {'Name':'Aung Aung','Age': 10}

del dict['Name']

print("Name :",dict["Name"])
print("Age :",str(dict["Age"]))

person1 = {'Name':'Aung Ko','Age':7}
person2 = {'Name':'Ko Ko','Age':9}


room = [person1,person2]
person2["Age"] = 11

for person in room:
	print("Name:"+person["Name"])
	print("Age:"+str(person["Age"]))
	print("======================")
	print(person)
	print("------------------")