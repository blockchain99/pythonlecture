# dictionaries are key value pairs that are useful 
# when describing collections and 
# order is not important.
# you can create dictionaries 
# with curly braces or the dict function.

# you can iterate over dictionaries 
# using keys(), values() and items()
# use methods like get to handle errors 
# more gracefully than 
# directly accessing keys in a dictionary



instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}
print(instructor["name"])
print("----------values()-------")
print(instructor.values)
for v in instructor.values():
    print(v)
print("--------keys()---------")
for k in instructor.keys():
    print(k)
print("------items(): key, value-----")
for k, v in instructor.items():
    print(k, v)
print("--------key in dictionary------") #key use just dictionary
print("name" in instructor) # True
print("awesome" in instructor) # False
print("--------value in dictionary--")
#value use dictionary.values()
print("Colt" in instructor.values()) # True
print("Nope!" in instructor.values() )# False

### make dictionary 
another_dictionary = dict(key = 'value')
print("another_dictionary :",another_dictionary) # {'key': 'value'}

{}.fromkeys("a","b") # {'a': 'b'}
{}.fromkeys(["email"], 'unknown') # {'email': 'unknown'}
{}.fromkeys("a",[1,2,3,4,5]) # {'a': [1, 2, 3, 4, 5]}

d = dict(a=1,b=2,c=3)
d['a'] # 1
d.get('a') # 1
d['b'] # 2
d.get('b') # 2
# d['no_key'] # KeyError
d.get('no_key') # None

print("=====dict(a=1,b=2,c=3)======--=====--")
d = dict(a=1,b=2,c=3)
print(d)
print("**** dictionary pop() need key")
# d.pop() # TypeError: pop expected at least 1 arguments, got 0
d.pop('a') # 1
print(d) # {'c': 3, 'b': 2}
# d.pop('e') # KeyError

#### Removes a random key in a dictionary:
d = dict(a=1,b=2,c=3,d=4,e=5)
print(d.popitem()) # ('d', 4)
# print(d.popitem('a')) # TypeError: popitem() takes no arguments (1 given)

### Update keys and values in a dictionary 
### with another set of key value pairs.
first = dict(a=1,b=2,c=3,d=4,e=5)
second = {}

second.update(first)
second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# let's overwrite an existng key
second['a'] = "AMAZING"

# if we update again
second.update(first) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# the update overrides our values
second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print("-------------------------------------")
numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key,value in numbers.items()}

print(squared_numbers) # {'first': 1, 'second': 4, 'third': 9}

print({num: num**2 for num in [1,2,3,4,5]}) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0,len(str1))} 
print(combo) # # {'A': '1', 'B': '2', 'C': '3'}

##conditional logic with dictionaries
num_list = [1,2,3,4]

{ num:("even" if num % 2 == 0 else "odd") for num in num_list }

# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}