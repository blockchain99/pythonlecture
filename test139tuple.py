#Tuple : unchaging value but same as list, has order, faster than lists, code safe.
#can not modify value, not remove value but can use index to access data
instructor = {  #dictionary 
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}
##return tuple from dictionary.items()
print(instructor.items())  #make tuple


print("###################################")
first_tuple = (1, 2, 3, 3, 3)

print(first_tuple[1])// 2
first_tuple[2] // 3
# print(first_tuple[-1]) // 3
print(first_tuple.count(3))
# second_tuple = tuple(5, 1, 2)

# second_tuple[0] # 5
# second_tuple[-1] # 2

first_tuple.index(3) #2

print("##########tuple###############")
names = ('Colt', 'Blue', 'Rusty', 'Lassie')

for name in names:
    print(name)

# Colt
# Blue
# Rusty
# Lassie
print("---------------------------------------")
months = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
i = len(months) -1
while i >= 0:
    print(months[i])
    i -=1

#Sets do not have duplicate values
# Elements in sets aren't ordered.
# You cannot access items in a set by index.
# Sets can be useful if you need to keep track of 
# a collection of elements, 
# but don't care about ordering, keys or values and duplicates.
# Sets cannot have duplictes
s = set({1, 2, 3, 4, 5, 5, 5}) # {1, 2, 3, 4, 5}

# Creating a new set
s = set({1, 4, 5})

# Creates a set with the same values as above
s = {1, 4, 5}

4 in s
# True

8 in s
# False
########### add for set###
s = set([1, 2, 3])

s.add(4)

s # {1, 2, 3, 4}

s.add(4)

s # {1, 2, 3, 4}
set1 = {1,2,3,4,5,6}

set1.remove(3)

print(set1) # {1, 2, 4, 5, 6}

s = set([1,2,3])
another_s = s.copy()
another_s # {1, 2, 3}
another_s is s # False

s = set([1, 2, 3])

s.clear()

s # set()
######### set comprehension########
{x**2 for x in range(10)}  #set
{x: x**2 for x in range(10)}  #dictionary

{char.upper() for char in 'hello'}
# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5
print(are_all_vowels_in_string("this is the world"))
########## |  & ###############
#union | , intersection & for two sets

############ ex############
# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1,2,3,4)
 
# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,) #type is tuple
value1 =(1) #type is int
 
# 3 - Given the following variable:
values = [10,20,30]
# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)
 
# 3 - Given the following variable
stuff = [1,3,1,5,2,5,1,2,5]
 
# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)