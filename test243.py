class Pet:
    allowed = ['cat','dog','pig','bird']
    def __init__(self, name, species):
        if species not in Pet.allowed:
        # if species not in self.allowed: #same as above.
            raise ValueError(f"You can have a {species} as pet.")
        self.name = name
        self.species = species
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError("You can have a {species} as pet.")
        self.species = species
cat = Pet("Blue", "cat")
dog = Pet("Lews", "dog")


# print(Pet("Tonny", "Tiger")) #ValueError: Your are not allowed...
doggy = Pet("Dorius", "dog")
print(doggy)
