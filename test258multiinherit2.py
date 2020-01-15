 #b#ad example: same property(name) in multiple places
class Aquatic:
    def __init__(self, name):
        print("AQUATIC INIT")
        self.name = name  # bad example define name in multiple class

    def swim(self):
        return f"{self.name} can swim."
    
    def greet(self):
        return f"I am {self.name} of the sea."
        
class Ambulatory:
    def __init__(self, name):
        print("Ambulatory INIT")
        self.name = name   #bad ex: same property(name) in multiple places

    def walk(self):
        return f"{self.name} can walk."
    
    def greet(self):
        return f"I am {self.name} of the land."

class Penguin(Ambulatory, Aquatic): #change order
    def __init__(self, name):
        print("Penguin INIT")
        super().__init__(name=name) #w/o self -> call Ambulatory, bad ex
        Aquatic.__init__(self,name=name) #with self -> then Aquatic, bad ex

# class Penguin(Ambulatory, Aquatic): #change order
#     def __init__(self, name):
#         print("Penguin INIT")
#         Ambulatory.__init__(self, name=name) #with self -> call Ambulatory, bad ex
#         Aquatic.__init__(self,name=name) #with self -> then Aquatic, bad ex

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


 
