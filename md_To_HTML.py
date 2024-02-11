import re

parser = re.compile("^#\\s(.*)")
text = "# Header 1"
replacement = parser.sub("<h1>\\1</h1>",text)
print(replacement)

text1 = "## Header 2"
replacement1 = re.sub("^##\\s(.*)","<h2>\\1</h2>",text1)
print(replacement1)

text2 = "This is **bold**. This is another **bold** again."
# replacement2 = re.sub("\*\*(.*?)\*\*","<b>\\1</b>",text2)
replacement2 = re.sub("\\*\\*(.*?)\\*\\*","<b>\\1</b>",text2)
print(replacement2)

text3 = "This is _italic_.And this is another _italic_ again."
replacement3 = re.sub("_(.*?)_","<i>\\1</i>",text3)
print(replacement3)