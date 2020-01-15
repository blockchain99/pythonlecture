class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"
class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"
        
# class Child(Mother, Father):  #lec ver
#     pass

class Child(Mother, Father):
    def __init__(self):
        super().__init__()

print(Child.__mro__)
# print(Child.mro())
# print(help(Child))
achild = Child()
print(achild.eye_color)
print(achild.hair_color)
print(achild.hair_type)