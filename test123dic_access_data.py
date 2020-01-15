artist = {
    "first": "Neil",
    "last": "Young",
}
full_name = artist.get("first")+' '+artist.get("last")
print(full_name)

print("===============join============")
words = ['Coding', 'Is', 'Fun!']
words1 = ' '.join(words) # 'Coding is Fun!'
print(words1)
name = ["Mr", "Steel"]
name2 = '. '.join(name)
print(name2)
print("----------join just key in dict----")
full_name1 = ' '.join(artist)
print(full_name1)

print("----------join just values in dict----")
full_name1 = ' '.join(artist.values())
print(full_name1)
print("----------format--------")
full_name = "{} {}".format(artist["first"],artist["last"])

full_name = f"{artist['first']} {artist['last']}"

print("==========total donation============")
# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!
print(donations)

total_donations = 0
for x in donations.values():
    total_donations += x
print(total_donations)

from functools import reduce
total_donations = reduce(lambda x,y: x + y, donations.values() )
print(total_donations)

total_donations = sum(donation for donation in donations.values())
total_donations = sum(donations.values())

# Use a loop to add together all the donations and 
# store the resulting number in a variable called total_donations

print("-------map-applies a function to all the items in an input_list")
upper_words1=[]
out = map(lambda x: x[0].upper()+x[1:], words)
print(out)
upper_words2 = list(out)
print(upper_words2)

print("----map---------")
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

squared = list(map(lambda x: x**2, items))

print("---function is list : x is function*multiply, add-------")
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
#######################################
#reduce applies a rolling computation to sequential pairs of values in a list
print("=========reduce:add or product=========")
product = 1
list_obj = [1, 2, 3, 4]
for num in list_obj:
    product = product * num
print(f"for loop product: {product}")
# product = 24

from functools import reduce
# import operator
from operator import add
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)
# add1 = reduce( operator.add, [1, 2, 3, 4] )
add1 = reduce( add, [1, 2, 3, 4] )
print(f"add1:{add1}")

# mul = reduce(lambda x,y: x*y, [1,2,3,4])
# print(mul)
# mul1 = reduce( operator.mul, [1, 2, 3, 4] )
# print(mul1)

#####################filter#########
fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
even = filter(lambda x: x % 2 == 0, fibonacci)  
odd_numbers = list(filter(lambda x: x % 2, fibonacci)) # x%2 -> 1 -> T
print(even)
result = list(even)
print(result)
print(odd_numbers)

#############create key-value pairs from comma separated values:####
### make a new dict from fromkeys()
answer = {}.fromkeys(['a','e','i','o','u'], 0)
answer = dict.fromkeys("aeiou", 0) 
print(answer)
comsep = ['name', 'score','email','profile bio']
new_user = {}.fromkeys(['name', 'score','email','profile bio'],'unknown')
print(new_user)
new_user1 = dict.fromkeys(comsep, 'unknown')
print(new_user1)
other = new_user.fromkeys(['phone'], 'unknown')
print(other)
other1  = new_user.fromkeys('phone', 'unknown')
print(other1)
other2  = new_user.fromkeys(range(1, 10), 'unknown')
print(other2)
print(new_user)

print("################################exercise=======")
# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

############# wrong prog ##############
print(f"{food} is choosed!")
# YOUR CODE GOES BELOW:
for k,v in bakery_stock.items():
    if k == food:
        print(f"{k} is {v} left")
    else:
        print("We don't make that")   #multiple show We dont't... -> wrong programming 

print("--------2nd----------------")
############# correct one!! ##############
print(f"{food} is choosed!")

if food in bakery_stock:
    print(f"{food} is {bakery_stock[food]} left")
    # print(f"{food} is {bakery_stock.get(food)} left")
else:
    print("We don't make that") 
        
print("###################Fromkeys exercise##########")
#DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", 
"items_in_inventory", "power_ups", "ammo", "enemies_on_screen", 
"enemy_kills", "enemy_kill_streaks", "minutes_played", 
"notifications", "achievements"] 

# Use the game_properties list and dict.fromkeys() 
# to generate a dictionary with all values set to 0. 
# Save the result to a variable called initial_game_state
initial_game_state = {}.fromkeys(["current_score", "high_score", "number_of_lives", 
"items_in_inventory", "power_ups", "ammo", "enemies_on_screen", 
"enemy_kills", "enemy_kill_streaks", "minutes_played", 
"notifications", "achievements"] ,0)            
print(initial_game_state)
initial_game_state = dict.fromkeys(game_properties, 0)
print(initial_game_state)

print("+++++++++++++++ update +++++++++++")
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

person = {"city": "Antigua"}
person.update(instructor)
print(person)
print(instructor)
person['name']= "Evelia"
print(person)
person.update(instructor)
print(f"** after updaed again with instructor: {person}")
print("################popitem, update##############")
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

### Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD

stock_list = inventory.copy()
print(stock_list)

# stock_list = {}
# stock_list.update(inventory)
# print(stock_list)

# add the value 18 to stock_list under the key "cookie"
stock_list["cookie"] = 18
stock_list.update(inventory)
print(stock_list)

# remove 'cake' from stock_list USE A DICTIONARY METHOD

stock_list.pop('cake')
print(stock_list)