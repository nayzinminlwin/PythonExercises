list = [1,2,3,4,5,6,7,8,9]

print("Total room in array is",len(list))
result = 0;

#for x in range(len(list)):
	# print(x,"room is",list[x])
	# result = result + list[x]

#for loop in array also work as follow. it is for each loop.
for x in list:
	result = result + x

print("The sum of the array is",result)

#in for each loop, 
#we cant know the index of current poisition like it is index 0 or 1 or 2
print("To know the index in ForEach loop, we use Enumerate keyword!")

for (y,value) in enumerate(list):
	print("Index :",y,"And Value :",value)