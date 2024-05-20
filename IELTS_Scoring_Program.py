# IELTS Scoring Program
import math

def gradingExe(markInput):

	grading = 0.0
	try:
		markInput = int(markInput)

		if markInput :
			if markInput<=5 and markInput>=0:
				grading = 2.5
			elif markInput<=7:
				grading = 3
			elif markInput<=9:
				grading = 3.5
			elif markInput<=12:
				grading = 4
			elif markInput<=14:
				grading = 4.5
			elif markInput<=18:
				grading = 5
			elif markInput<=22:
				grading = 5.5
			elif markInput<=26:
				grading = 6
			elif markInput<=29:
				grading = 6.5
			elif markInput<=32:
				grading = 7
			elif markInput<=34:
				grading = 7.5
			elif markInput<=36:
				grading = 8
			elif markInput<=38:
				grading = 8.5
			elif markInput<=40:
				grading = 9
			else:
				print("The mark should be between 0 and 40.")
				pass
		else:
			print("Wrong Input!!")
			pass

		return grading

	except ValueError:
		print("Input must be numbers only!")

def rounding_exe(TotalBand):
	int_part = int(TotalBand)
	frac_part = TotalBand - int_part

	if frac_part < 0.25:
		return float(int_part)
	elif frac_part < 0.75:
		return float(int_part)+0.5
	else :
		return float(int_part)+1.0

print("")
print("IELTS Scoring Program")
print("======================")

listening_mark =input("How many corrects out of 40 in Listening :")
listening_grade = gradingExe(listening_mark)
print("Your IELTS Listening band score is",float(listening_grade))
print("--------------------------------------")

reading_mark = input("How many corrects out of 40 in Reading :")
reading_grade = gradingExe(reading_mark)
print("Your IELTS Reading band score is",float(reading_grade))
print("-------------------------------------")

writing_grade =input("Band score of Writing :")
print("Your IELTS Writing band score is",float(writing_grade ))
print("-------------------------------------")

speaking_grade =input("Band score of Speaking :")
print("Your IELTS Speaking band score is",float(speaking_grade ))
print("--------------------------------------")

total_band = 0.0
try :
	total_band = (listening_grade+reading_grade+float(writing_grade)+float(speaking_grade))/4
	total_band = rounding_exe(total_band)
	print("Your IELTS Total Band score is",total_band)
	print("===================================")

except ValueError and TypeError:
	print("Total IELTS band score can't be calculated!")
	print("Input must be numbers only!")
	print("===========================================")

input("Press Enter to exit . . .")