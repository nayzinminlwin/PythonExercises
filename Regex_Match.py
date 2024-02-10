import re

# telenor = re.compile("(\+?95|0?9)7(9|8|7)\d{7}$")

Atom = re.compile("(\+95|0)9(7|8|9)[0-9]{8}$")

if Atom.match("+959755511977") == None:
	print("Not Atom Number!")
else:
	print("Atom Number Confirmed!")

if Atom.match("09971234567") == None :
	print("Not telenor")
else:
	print("telenor")