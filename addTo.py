
a = int(input("Enter 1st number u start to add :"))
b = int(input("Enter 2nd number u end up adding :"))

pairs = (b-a)/2 
midNum = (a+b)/2

# if type(midNum)==int :
if (a+b)%2 == 0:
	result = ((a+b)*pairs)+midNum
	print("Passed if")

else :
	result = (a+b)*(pairs + 0.5)
	print("Passed else")

print("Algorithm result is",result)



for x in range(a,b):
 a = a + x + 1
print("The true result is",a)