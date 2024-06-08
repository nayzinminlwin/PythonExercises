import markdown 
from pathlib import Path

md_path = str(input("Enter path of md file: "))

try :
	md_file = Path(md_path)
	markdown_text = md_file.read_text()

	html_text = markdown.markdown(markdown_text)

	html_file = Path('ConvertedHTML.html')
	html_file.write_text(html_text)

	print("Successfully converted markdown file to HTML!")

except ValueError:
	print("Enter the file path correctly!")

input("Press Enter to exit.")