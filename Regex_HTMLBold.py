import re

bold_regex = re.compile(".*<b>(.*)</b>.*")

text = "Hello <b>World</b>"

match = bold_regex.match(text)

print(match)
print(match.group(0))
print(match.group(1))

bold_regex1 = re.compile("<b>(.*?)</b>")

text1 = "Hello <b>World</b>! This is <b>bold</b>."

match1 = bold_regex1.findall(text1)
print(match1)

