# This program will prepare an Answer Sheet for IELTS practice and export in .txt format 
from datetime import datetime
from pathlib import Path
import os

def preparationFunction():
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

		#directory allocation
		current_dir = Path(os.path.dirname(os.path.abspath(file_name)))
		os.chdir(current_dir)

		# file_path =Path(os.path.join(current_dir,output_file))
		file_path = Path(current_dir)/file_name
		# print("1. Cureent file path is "+ str(file_path))

		

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
			one_to_4ty = one_to_4ty+str(x)+". \n"
			pass

		# final text into the file
		text_into_file = book + " " +test + "\n"+ current_time_str + "\n \n" + Ltn_or_Rd+ "\n \n" + one_to_4ty
		# print(text_into_file)

		# gonna parse text into file
		file_path.write_text(text_into_file)
		print("Answer sheet for your IELTS practice is exported!")

	except ValueError:
		print("Enter the inputs correctly!")

	prepareAgain()
	pass


def prepareAgain():
	again = str(input("U want to create another ans paper ?(y or n) :"))
	# print("Inserted value is "+ again)

	if again in ["y","Y","yes","YES"]:
		# print("I see yes!")
		preparationFunction()
	else :
		# print("I see sth else!")
		input("Now press Enter to exit!")
		pass
	pass

preparationFunction()