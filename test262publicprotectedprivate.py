#Python doesn’t have any mechanisms, that would effectively 
# restrict you from accessing a variable or calling 
# a member method. 

print("=============public===============")
#All member variables and methods are public by default in Python.
# So when you want to make your member public, 
# you just do nothing.
class Cup:
    def __init__(self):
        self.color = None
        self.content = None

    def fill(self, beverage):
        self.content = beverage

    def empty(self):
        self.content = None
    def __repr__(self):
        # return self.content
        return f"content {self.content} with color {self.color}"

redCup = Cup()
redCup.color = "red"
redCup.content = "tea"
print(f"--{redCup}") 
redCup.empty()
redCup.fill("coffee")
print(f"--{redCup}") 

print("============protectd=============")
# __member_var_name  -> protected
# you’re telling others “don’t touch this, 
# unless you’re a subclass”

class Cup2:
    def __init__(self):
        self.color = None
        self._content = None # protected variable

    def fill(self, beverage):
        self._content = beverage

    def empty(self):
        self._content = None
    
    def __repr__(self):
        # return self.content
        return f"content {self._content} with color {self.color}"

# same example as before, but the content of the cup is 
# now protected. This changes virtually nothing, 
# you’ll still be able to access the variable 
# from outside the class, only if you see 
# something like this:

# you explain politely to the person responsible for this, 
# that the variable is protected and he should not access it 
# or even worse, change it from outside the class.

cup2 = Cup2()
cup2._content = "tea"
print(cup2._content)
print(cup2)


print("=============private===============")
# By declaring your data member private you mean,
#  that nobody should be able to access it 
# from outside the class, i.e. 
# strong you can’t touch this policy. 
class Cup3:
    def __init__(self):
        self.color = None
        self.__content = None # protected variable

    def fill(self, beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None
    
    def __repr__(self):
        # return self.content
        return f"content {self.__content} with color {self.color}"

# Our cup now can be only filled and poured out by 
# using fill() and empty() methods. Note, 
# that if you try accessing __content from outside, 
# you’ll get an error.
cup3 = Cup3()
cup3.fill("coffee")
print(cup3)
cup3.__content = "tea" #not overwriting to __content
print(cup3)
cup3._Cup3__content = "tea" #yes overwritng
print(cup3)

print("-------------------------------------------")
# Name   Notation   Behaviour
# name	 Public     Can be accessed from inside and outside
# _name	 Protected  Like a public member, but they shouldn't be directly accessed from outside.
# __name Private    Can't be seen and accessed from outside
print("=========------------")
class Encapsulation(object):
    def __init__(self, a, b, c):
        self.public_val = a
        self._protected_val = b
        self.__private_val = c

e = Encapsulation(1,2,3)
print(e.public_val)
e._protected_val = 20
print(e._protected_val)
