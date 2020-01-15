# Another class with a class attribute, used for validation purposes
#We can also define attributes directly on a class that are shared by 
# all instances of a class and the class itself.(allowed)
class Pet:
	
	allowed = ['cat', 'dog', 'fish', 'rat'] #to share by instance & class itself.

	def __init__(self, name, species): #properties: name, species
		##move to up level to share, then allowd-> Pet.allowed
		# allowed = ['cat', 'dog', 'fish', 'rat']
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species

	def set_species(self,species): #assign new species, which in allowed list
		if species not in Pet.allowed:  #share 'allowed'
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species
	
	def show_pet(self):
		return f" My pet is {self.name} and species {self.species}."
print("----------cat instance------------")
cat = Pet("Blue", "cat") #share 'allowed'
print(cat.species)
print(cat.show_pet())
### show cat's species cat.set_species("tiger") #ValueError , you cant not have a tiger pet!
print(Pet.allowed)
print("---------- dog instance -----------")
dog = Pet("Wyatt", "dog") #share 'allowed'
print(dog.show_pet())
print("==========overwriting species================")
## overwirting instance cat species to rat
cat.set_species("rat")
print(cat.show_pet())
print(cat.species)
print(Pet.allowed)
print("------ assign new species in 'allowd' list in class Pet---")
Pet.allowed.append("pig")
print(Pet.allowed)

print("=======(cat)instance of Pet can assign new species 'pig' \
	from 'allowed' appended in class Pet =========")
cat.set_species("pig") #assign pig to new species for instance cat.
print(f"** after assign pig to instance cat : {cat.species} ")
print(cat.show_pet())
print("------same id for cat(instance), Pet(class)-------")
print(Pet.allowed)
print(cat.allowed)
print(id(Pet.allowed))
print(id(cat.allowed))
print("------- calt.allowed -> change -----")
cat.allowed = ['tiger', 'bear']
print(cat.allowed) #cat has it's own version of allowed
print(Pet.allowed)
print(dog.allowed) #since dog,instance still referring attribute Pet.allowed in class

print("*************")
#Not using set_species just overwriting property.
dog.species = "tiger" #overwirting property species after initialzling 
print(dog.show_pet())
