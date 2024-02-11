import re

parser = re.compile("^#\\s(.*)")
text = "# Header 1"
replacement = parser.sub("<h1>\\1</h1>",text)
print(replacement)

text1 = "## Header 2"
replacement1 = re.sub("^##\\s(.*)","<h2>\\1</h2>",text1)
print(replacement1)