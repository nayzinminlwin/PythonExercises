class animal:
	numberOfLegs = 0

	def __init__(self,legs=4):
		self.numberOfLegs = legs

	def sleep(self):
		print("zzz")

	def countLegs(self):
		print("i have {} legs".format(self.numberOfLegs))

# dog = animal()
# dog.numberOfLegs = 4

# print("Dog has {} legs.".format(dog.numberOfLegs))
# print("Dog has",dog.numberOfLegs,"legs.")
# print("Dog has",str(dog.numberOfLegs),"legs.")

# dog.sleep()

# spider=animal(8)

# print("Spider has {} legs.".format(spider.numberOfLegs))

class dog(animal):

	def __init__(self):
		numberOfLegs = 4

	def bark(self):
		print("Woof Woof!")

myDog = dog()
myDog.sleep()
myDog.bark()