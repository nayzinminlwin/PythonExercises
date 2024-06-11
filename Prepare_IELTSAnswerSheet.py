# This program will prepare an Answer Sheet for IELTS practice and export in .txt format 

from pathlib import Path

try :
	book = str(input("Which IELTS Book are you practicing : "))
	testNum = int(input("Test number :"))

	print("What U gonna practice Listening or Reading ?")
	Ltn_or_Rd = str(input("Enter 'L' for Listening , 'R' for Reading :"))

	if Ltn_or_Rd == "L" or Ltn_or_Rd == "l" or Ltn_or_Rd == "Listening" or Ltn_or_Rd == "listning":
		Ltn_or_Rd = "Listening"

	elif Ltn_or_Rd == "R" or Ltn_or_Rd == "r" or Ltn_or_Rd == "Reading" or Ltn_or_Rd == "reading":
		Ltn_or_Rd = "Reading"

	else :
		Ltn_or_Rd = "Unknown"

	test = "Test"+testNum

except ValueError:
	print("Enter the inputs correctly!")

input("Press Enter to exit!!")