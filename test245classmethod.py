#class methods are mothods(with @classmethod) that are 
#not concerned with instances, but the class itself.
# class method used when the method does not need to know about
# the specific instance; 

class User:

	active_users = 0

	# @classmethod
	# def display_active_users(cls): #not instance user, actually class user
	# 	print(cls)

	@classmethod
	def display_active_users(cls): #not instance user, cls:actually class user(User.blabla)
		return f"There are currently {cls.active_users} active users."

	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		##instead User(first, l,a) -> cls(f,l,a)
		return cls(first, last, int(age))#create new instance of class
	
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		# self.age = int(age)
		User.active_users += 1

	def __repr__(self): #turning into readable format. 
		return f"{self.first} is {self.age} . "

	def show_age(self):
		return  f"{self.first} is {self.age} . "

	def logout(self):
		User.active_users -= 1  #refer class attribute active_users
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):  #make age an int ?
		self.age += 1
		return f"Happy {self.age}th, {self.first}"


# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)

# # print(user1.display_active_users()) #same result with below line.(instance.class_method)
# # print(User.display_active_users()) #class_name.class_method

# print(User.display_active_users())

# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)

# print(User.display_active_users())


####################### csv file #######################
#"Tom,Jones,89"
tom = User.from_string("Tom,Jones,89")
print(tom.first)
print(tom.full_name())
print(tom.birthday())

print("---- __repr__ ---")
sam = User.from_string("Sam,Jane,46")
# print(sam)  #w/o __repr__  ->    < main .User obje ...
print(sam)  #with __repr__  (custom representation)->  

print("--- not instance from User.from_string, but User('Judy')---")
j = User("Judy", "steel", 18)
print(j)
j = str(j) #even though 18 is converted to string, 
print(j)  #it can be printed since __repr__ converted str to int

print("----------j1.show_age()-----------------")
j1 = User("Judy", "steel", 18)
j1=str(j1)
# print(j1.show_age()) #AttributeError : 'str' has no attrbute 'show_age'

