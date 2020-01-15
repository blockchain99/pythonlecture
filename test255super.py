# Inheritance Example Using Super()
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, species, breed, toy):
        # self.name = name
        # self.species = species
		Animal.__init__(self, name, species)
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")

print("------Animal.__init__(name, species)------")
blue = Cat("Blue","Cat", "Scottish Fold", "String")
print(blue)
print(blue.species)
print(blue.breed)
print(blue.toy)


# OUR "MODEL" FOR ANIMAL AND CAT
# Animal
# 	species
# 	name

# Cat
# 	species
# 	name
# 	breed
# 	favorite_toy