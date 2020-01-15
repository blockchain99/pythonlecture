#age : not private, use in an outside class
#_age : private: internal use in this class
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self.age = age
        else:
            self.age = 0

jane = Human("Jane", "Goodwill", 50)
print(jane.age)
print("------- negativ age-------")
jane = Human("Jane", "Goodwill", -9)
print(jane.age)
