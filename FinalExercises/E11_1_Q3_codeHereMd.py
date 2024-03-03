import re

text = "Hello 'Code Here' World"

replacementText = re.sub("'(.*)'","<code>\\1</code>",text)

print(replacementText)