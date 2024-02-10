import re

bold_regex = re.compile(".*<b>(.*)</b>.*")

text = "Hello <b>World</b>"

match = bold_regex.match(text)

print(match)
print(match.group(0))
print(match.group(1))