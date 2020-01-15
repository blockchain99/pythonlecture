class Aquatic:
    def __init__(self, name):
        print("AQUATIC INIT")
        self.name = name

    def swim(self):
        return f"{self.name} can swim."
    
    def greet(self):
        return f"I am {self.name} of the sea."
        
class Ambulatory:
    def __init__(self, name):
        print("Ambulatory INIT")
        self.name = name

    def walk(self):
        return f"{self.name} can walk."
    
    def greet(self):
        return f"I am {self.name} of the land."

class Penguin(Aquatic, Ambulatory):
    def __init__(self, name):
        print("Penguin INIT")
        super().__init__(name=name) #w/o self

print("=======================test 1======")
jaws = Aquatic('jaws')
print(jaws.greet())
print("--------------")
lassie = Ambulatory('lassie')
print(lassie.walk())
print("--------------")
p = Penguin("pengoo")
print(p.greet())
print(p.swim())
print(p.walk())
print(f"*** which greet() call ? : {p.greet()}")
print(Penguin.__mro__) #classname.__mro__, mro(classname), help(classname)
print("--------------")
print(f" p is instance of Penguin: {isinstance(p, Penguin)}")
print(f" p is instance of Aquatic: {isinstance(p, Aquatic)}")
print(f" p is instance of Penguin: {isinstance(p, Ambulatory)}")


 
