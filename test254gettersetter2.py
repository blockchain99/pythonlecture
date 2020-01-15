
#_age : private: internal use in this class
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    def get_age(self): #to access private _age: need get method
        return self._age

    def set_age(self, new_age):#to set private _age : set method
        if new_age >= 0:
            self._age = new_age
        else:
            self._age = 0

print("------- negativ age-------")
jane = Human("Jane", "Goodwill", -9)
# print(jane.age) #error, AttributError, no .age method
print(jane.get_age())
jane.set_age(45)
print(jane.get_age())
