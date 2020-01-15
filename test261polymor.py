#Ploymorphism & inheritance
#mothod(speak()) overriding - each subclass will have 
# a different implementation of the mothod

## error -> ctrl shit p -> convert indentation to tab
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")

	def speak(self):
		raise NotImplementedError("Subclss need to be implemented")

class Dog(Animal):
	def __init__(self, name, species, breed, toy):
		# self.name = name
		# self.species = species
		Animal.__init__(self, name, species)
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")

###TypeError: speak() missing 1 required 
### positional argument:'name'
###	def speak(self, name): #no need name

	def speak(self):
		return f"{self.name} speaks woof"

class Cat(Animal):
	def __init__(self, name, species, breed, toy):
		# self.name = name
		# self.species = species
		Animal.__init__(self, name, species)
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")

	def speak(self):
		return f"{self.name} speaks meow"

print("------Animal.__init__(name, species)------")
blue = Cat("Blue","Cat", "Scottish Fold", "String")
print(blue)
print(blue.species)
print(blue.breed)
print(blue.toy)
# print(blue.play())
print(blue.speak())
blue.make_sound("yahoo")

print("------Animal.__init__(name, species)------")
doggy = Dog("Paker","Dog", "James Bond", "Ball")
print(doggy)
print(doggy.species)
print(doggy.breed)
print(doggy.toy)
# print(doggy.play())
print(doggy.speak())

print(" ** object can take on many(poly) forms( morph) ")
print("============= special method==========")
print("-------- 8 +2 ->10 vs '8' + '2'-> 82 =====")

print("-----same class method for different class -----")
print(Cat("Blue","Cat", "Scottish Fold", "String").speak())
print( Dog("Paker","Dog", "James Bond", "Ball").speak())

print("---- same operation for different object------")
sample_list = [1,2,3]
sample_tuple = (1,2,3)
sample_string = "awesome"

print(len(sample_list))
print(len(sample_tuple))
print(len(sample_string))