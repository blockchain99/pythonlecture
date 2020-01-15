
#_age : private: internal use in this class
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # def get_age(self): #to access private _age: need get method
    #     return self._age

    # def set_age(self, new_age):#to set private _age : set method
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_value):
        if new_value >= 0:
            self._age = new_value
        else:
            # self._age = 0
            raise ValueError("age can't be negative")
    @property
    def full_name(self):
        return f"Full name is {self.first} {self.last}"
   ########### one string splitted into 2 parameters ############# 
    # @full_name.setter
    # def full_name(self, new_name):
    #     self.first, self.last = new_name.split(" ")

############ using a tuple with two parameters #########
    @full_name.setter  
    def full_name(self, new_name):
        self.first, self.last = new_name

print("------- negativ age-------")
jane = Human("Jane", "Goodwill", 30)
# # print(jane.age) #error, AttributError, no .age method
# print(jane.get_age()) 
# jane.set_age(45)
# print(jane.get_age())

print(jane.age) #just attribute not method, no age()
jane.age = 20 
print(jane.age)
print(jane.full_name) 
# print("-------- set using blank sperated arguments ----")
# jane.full_name = "James Dean"  
# print(jane.full_name)
# print(jane.__dict__)
print("-------- set using tuple-----")
jane.full_name = ("James", "Dean")
print(jane.full_name)
print(jane.__dict__)
  
