#__init__ method is called every time instance is created(creating obj)
#  -> instanciate a class :  
# self refers to current class instance
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year
    
car = Vehicle("Toyota","Sienna",2005) #__init__ is called
boat = Vehicle("Hyundai","Bigboat",2012) #__init__ is called
print(car.make)
print(boat.model)
print(car.year)