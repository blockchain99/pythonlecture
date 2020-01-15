import random

rn = random.choice(["apple", "banana", "cherry", "durian"])
sh =random.shuffle(["apple", "banana", "cherry", "durian"])
print(rn)
print(sh)
fruits = ["apple", "banana", "cherry", "durian"]
print(fruits)
random.shuffle(fruits) #make suffle originale list and save as changed list.
print(fruits)

print("------- import as -------")
import random as my_own_random
print(my_own_random.choice(fruits))