import re

text = "K/12344/32"

if re.match("[A-Z]\\/[0-9]{5}\\/[0-9]{2}",text)==None:
	print("Not Match!")
else:
	print("Match!")