import re

parser = re.compile("^#\s(.*)")
text = "# Header 1"
replacement = parser.sub("<h1>\\1</h1>",text)
print(replacement)
