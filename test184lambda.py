# A regular named function
def square(num): return num * num

# An equivalent lambda, saved to a variable
square2 = lambda num: num * num

# Another lambda
add = lambda a,b: a + b

# Executing the lambdas
print(square2(7))
print(add(3,10))

# Notice that the square function has a name, but the two lambdas do not
print(square.__name__)
print(square2.__name__)
print(add.__name__)

##########
# Write a lambda that accepts a single number and cubes it. Save it in a variable called cube.
cube = lambda x : x ** 3

print("###### map : std func accepts at least two arguments, a func and an 'iterable'")
print("## iterable : something taht can be iterated over \
      (lists, sirings, dictionaries, sets, tuples) -> return as map obj -< convert to \
      another data structure(list, ...)")
nums = list(range(2,11,2))
print(nums)
doubles_map_obj = map(lambda num: num*2 , nums)
print(doubles_map_obj)
for x in doubles_map_obj:
    print(x)
print(list(doubles_map_obj)) #already used above for loop, so it is empty list..
print(list( map(lambda num: num*2 , nums)))

print("==============------conver to upper case ")
people=["Darcy", "Christin", "Dane", "Annabel"]
upper = list(map(lambda x: x.upper(), people))
print(upper)

print("----------map with dict-------")
### list of dictionary ####
names = [
    {'first':'Rusty', 'last': 'Steele'}, 
    {'first':'Colt', 'last': 'Steele', }, 
    {'first':'Blue', 'last': 'Steele', }
]

print(type(names))
# print(names.get('first', 'no name')) #error : list no method get(since get for dict)
print([x.get('first', 'no key') for x in names]) #x is dictionary, if not exit return None but I declare as no key
print([x['first'] for x in names]) 
print(list(map(lambda x:x['first'] ,names)))
# first_names = list(map(lambda x: x.get(first), names))

# print(first_names) # ['Rusty', 'Colt', 'Blue']

print("########filter#######")
l = [1,2,3,4]
m = [3,4,5,6]
evens = list(filter(lambda x: x % 2 == 0, l))
evens1 =[x for x in l if x % 2 == 0]
evens2 =['even' if x % 2 ==0 else 'false' for x in range(1, 5)]
evens3 =[[x for x in range(1,5)] for x in range(1, 5)]
intersect = [ x for x in l if x in m]
print(evens) # [2,4]
print(evens1) # [2,4]
print(evens2) # 
print(evens3) # 
print(intersect)

print("######## combining finter and map######")
# Return a new list with the string
# "Your instructor is " + each value in the array,
# but only if the value is less than 5 characters
names = ['Lassie', 'Colt', 'Rusty']
comb = [ 'Your instructor is '+ x for x in names if len(x) < 5]
# [f"Your instructor is {name}" for name in names if len(name) < 5]
print(comb)

comb_filter = list(filter(lambda x: len(x) < 5, names))
# comb_filter = filter(lambda x: len(x) < 5, names) #obj
print(comb_filter)
comb1 = list(map(lambda x: f"Your instructor is {x}", comb_filter))
print(comb1)

print("------ one line with map and filter")
comb2 = list(map(lambda x: f"Your instructor is {x}",filter(lambda x: len(x) < 5, names)))
print(comb2)

print("########## reduce: ")
# runs a function of two arguments cumulatively to the items of iterable, 
# from left to right, which reduces the iterable to a single value
from functools import reduce
l = [1,2,3,4]
product = reduce(lambda x, y: x * y, l)
print(product)
l = [1,2,3,4]
total = reduce(lambda x, y: x + y, l, 10) #sum from 10
print(total)
total1 = reduce(lambda x, y: x + y, l) 
print(total1)

print("----------partial app with clousures------")
def outer(a):
    def inner(b):
        return a+b
    return inner

result = outer(10)

print(result(20)) # 30

##all: Return True if all elements of the iterable are truthy 
# (or if the iterable is empty)
all([0,1,2,3]) # False

all([char for char in 'eio' if char in 'aeiou'])

all([num for num in [4,2,10,6,8] if num % 2 == 0]) # True

#any : Return True if any element of the iterable is truthy. 
# If the iterable is empty, return False

#list(sorted([..])), list(reversed([..])), max([..]),sum([..])
print('awesome')
print(max('awesome'))
print(max({1:'a', 3:'c', 2:'b'}))
print(sum([1,2,3,4], -10))
print("---------- round -----------")
## round : Return number rounded to ndigits precision after the decimal point. 
# If ndigits is omitted or is None, it returns the nearest integer to its input.
print(round(10.2)) # 10
print(round(1.212121, 2)) # 1.21

print("########## zip##########")
first_zip = zip([1,2,3], [4,5,6])

list(first_zip) # [(1, 4), (2, 5), (3, 6)]

dict(first_zip) # {1: 4, 2: 5, 3: 6}
print("--------unzip----------")
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*five_by_two)))
# [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

nums1 = [1,2,3]
nums2 = [20,14,11]
def decrement_list(nums):
    # return [x-1 for x in nums]
    return list(map(lambda x: x-1, nums)) #lec ver

print(decrement_list(nums1))
print(decrement_list(nums2))

print("--------- filter ex-------")

def remove_negatives(nums):
    return [x for x in nums if x >= 0]
    # return list(filter(lambda x: x>= 0,nums)) #lec ver
print(remove_negatives([-1,3,4,-99]))
print(remove_negatives([-7,0,1,2,3,4,5]))

print("-------------all----------")

print([char for char in 'eio' if char in 'aeiou'])
print(all([char for char in 'eio' if char in 'aeiou'])) #all 'eio' elements are in 'aeiou' 

people= ["Chale", "Crhist", "Chone", "Cathy"]
print(all([name[0]=='C' for name in people]))
people.insert(1,"Kitty")
print(all([name[0]=='C' for name in people]))

print("=======")
nums5 = [2,60,26,18,21]
print(all([num % 2 ==0 for num in nums5]))

print("======only string=======")
def is_all_strings(st):
    return all([isinstance(x, str) for x in st ]) #python 3.x
    # return all([isinstance(x, basestring) for x in st ]) #python 2
    # return all([type(l) == str for l in lst])  #lec ver
print(is_all_strings(['a','b','c']))
print(is_all_strings([2, 'k','b','c']))
print(is_all_strings(['hello', 'good buy']))

print("------------ sorted --------------")
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# To sort users by their username
sorted(users,key=lambda user: user['username'])

# Finding our most active users...
# Sort users by number of tweets, descending
sorted(users,key=lambda user: len(user["tweets"]), reverse=True)

# ANOTHER EXAMPLE DATA SET==================================
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# To sort songs by playcount
sorted(songs, key=lambda s: s['playcount'])

print("--------- interleaving string--------")
print("== seperator.join(iterable such as list)==: seperator is '' ")
#interleave('h1' 'ha') -> 'hhia'
def interleave(s1, s2):
    zipstr = list(zip(s1,s2)) #*[('h', 'h'),('i','a')"]
    print(zipstr)
    newstr = [''.join(x) for x in zipstr] 
    # for each-('h', 'h'),('i','a')-join:'h', 'h'  -> ['hh', '1a']
    print(newstr)
    print("--- list output----")
    newstr1 = [''.join(newstr)] #['hh', '1a']
    print(newstr1)
    print("--- just string ---")
    newstr1 = ''.join(newstr) #hh1a
    print(newstr1)


interleave('h1', 'ha')
print("---------my ver---------")
def interleave2(str1, str2):
    return  ''.join( ''.join(x) for x in zip(str1, str2)) 
    #('h', 'h'),('i','a') -> for each element join : 'hh','ia'-> join two : 'hhia'


print(interleave2('h1', 'ha'))


print("=======lec ver====")

def interleave1(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))
print(interleave1('h1', 'ha'))

print("-----filter out num not divide by 4-> remaining numbers divide by 4 -> *3---------")
'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(nums):
    return list(map(lambda x: x*3 , filter(lambda x: x % 4 == 0, nums)))

print(triple_and_filter([1,2,3,4]))
print(triple_and_filter([6,8,10,12]))

def triple_and_filter1(nums):
    return [ x *3 for x in nums if x %4 ==0]

print(triple_and_filter1([1,2,3,4]))
print(triple_and_filter1([6,8,10,12]))

print("# =====dict.get(..) test=====")
'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(names[0].get('first'))
for adic in names:
    print(f"{adic.get('first')} {adic.get('last')}")

print("------ list version-------")
# def extract_full_name(alist): #list, not dict!!
#     for adic in alist:  # a is dict
#         return [f"{adic.get('first')} {adic.get('last')}"] #-> multiple (first+second)

def extract_full_name(alist): #list, not dict!!
    return [f"{adic.get('first')} {adic.get('last')}" for adic in alist]
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']

def extract_full_name1(l):  #lec ver
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))
print("# =========make ref **kwargs==================")
###########use ** as an argument:Dictionary unpacking######
# def display_names(first, second):
#     print(f"{first} says hello to {second}")

def display_names(**kwargs):
    print(f"{kwargs.get('first')} says hello to {kwargs.get('second')}")

display_names(first="James", second="Tom") #must same as func parameter.

names = {"first": "Colt", "second":"Joshua"}
# display_names(names) #error: just 1 arg(dict itself) instead of 2 elements
display_names(**names) #unpacking dict
# ==============================================







