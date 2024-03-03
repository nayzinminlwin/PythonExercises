import re

text = "@mgmg"

replacementText = re.sub("@(.*)\\s*","<a href=\"/username/\\1\">@\\1</a>",text)

print(replacementText)