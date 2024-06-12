# This program will prepare an Answer Sheet for IELTS practice and export in .txt format 
from datetime import datetime
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

	# file construction
	test = "Test "+ str(testNum)
	file_name = "Test"+str(testNum)+"_"+str(Ltn_or_Rd)+".txt"
	print(file_name)
	output_file = Path(file_name)

	# lets work with date time 
	current_time =datetime.now()
	current_date = str(current_time.day)+"."+str(current_time.month)+"."+str(current_time.year)
	# print(current_date)
	current_hr_min = current_time.strftime('%I:%M %p')
	# print(current_hr_min)

	current_time_str = str(current_date) + " ("+current_hr_min+")"

	# gonna write 1 to 40
	one_to_4ty = ""
	for x in range(1,41):
		one_to_4ty = one_to_4ty+str(x)+".\n"
		pass

	# final text into the file
	text_into_file = book + " " +test + "\n"+ current_time_str + "\n \n" + Ltn_or_Rd+ "\n \n" + one_to_4ty
	# print(text_into_file)

	# gonna parse text into file
	output_file.write_text(text_into_file)
	print("Answer sheet for your IELTS practice is exported!")

except ValueError:
	print("Enter the inputs correctly!")

input("Press Enter to exit!!")