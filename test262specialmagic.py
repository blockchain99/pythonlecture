
#Python classes have special (also known as "magic") methods,
#  that are dunders (i.e. double underscore-named). 

#These are methods with special names that 
#give instructions to Python for how to deal with objects.

print(8 + 2 ) # 10
print("8" + "2" ) # 82
#The + operator is shorthand for a special method called
#  __add__() that gets called on the first operand.

#If the first (left) operand is an instance of int,
#  __add__() does mathematical addition. 
# If it's a string, it does string concatenation.

print("++++++++-your own special method+++++++")
#Therefore, you can declare special methods on your own classes 
# to mimic the behavior of builtin objects, 
# like so using __len__:
print("------ string w/o __repr__ ----")
class Human:
    def __init__(self, height, name="somebody"):
        self.height = height  # in inches
        self.name = name

    def __len__(self):
        return self.height

Colt = Human(60) 
print(len(Colt))  # 60

print(f"** looking ugly : {Colt}") #look ugly
print("------string with __repr__ -----")
class Human2:
    def __init__(self, height, name = "somebody"):
        self.height = height  # in inches
        self.name = name

    def __len__(self):
        return self.height

    def __repr__(self):
        return self.name

Colt2 = Human2(60) 
print(f"** looking good : {Colt2}")
