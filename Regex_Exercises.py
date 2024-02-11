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


# Exercise_1.3(code here)

theCoding = """'''js
var i = 0;
var k = 9;
var c = 99;
var t = 88;
'''"""
code = re.sub("'''(.*)(\n)+(.*)(\n)+'''","<code class=\"\\1\">\\2\\3</code>",theCoding)
print(code)
