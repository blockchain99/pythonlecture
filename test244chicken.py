#Keep track of how may eggs each indiviaul chkcken lays, 
# track total eggs all hens have laid. 
# lay_eggs(): increment & return particular Chicken's 'eggs' also
# increment class variable, 'total_eggs' 

#__init__ method is called every time instance is created(creating obj)
#  -> instanciate a class :  
# self refers to current class instance

class Chicken:
    total_eggs = 0 #share through instance and class
    def __init__(self, name, species):
        self.species = species
        self.name = name
        self.eggs = 0 

    def lay_eggs(self):
        self.eggs += 1
        Chicken.total_eggs +=1
        return self.eggs

c1 = Chicken(name = "Alice", species="Partridge")
c2 = Chicken(name = "Amica", species="Spckled")
print(Chicken.total_eggs)
c1.lay_eggs()
print(Chicken.total_eggs)
print(c2.lay_eggs())
print(c2.lay_eggs())
print(Chicken.total_eggs)

    
   