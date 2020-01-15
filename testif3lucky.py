from random import randint
choice = randint(1, 9)
if choice == 7:
    print("{} is lucky".format(choice))
else:
    print("{} is unlucky".format(choice))

num = randint(1, 1000)
if num % 2 == 0:
    print ("{} is even".format(num))
else:
    print (" {} is odd".format(num))
    
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm'])

if food == 'apple' or food == 'grape':
    print ("fruit")
elif food == 'bacon' or food == 'steak':
    print("meat")
else:
    print("yuck")