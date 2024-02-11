import re

# Exercise_1.1(Car License)

carPlate = re.compile("^[A-Z]/\\d{5}/\\d{2}$")

if carPlate.match("C/64429/89")==None:
	print("Not a car license plate!")
else:
	print("Valid license plate.")


# Exercise_1.2(Mention)

mentionText = "@MgMg How are you?"
text = re.sub("^@(.*?)\\s(.*)","<a href=\"/username/\\1\">\\1 \\2</a>",mentionText)
print(text)
