# NO TOUCHING ======================================

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# NO TOUCHING ======================================


calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if actually_sick and not sick_days :
# if actually_sick and sick_days > 0 :
    calling_in_sick = True
elif kinda_sick and hate_your_job and not sick_days:
# elif kinda_sick and hate_your_job and not sick_days > 0:
    calling_in_sick = True
else:
    calling_in_sick = False
print (" As for actually_sick: {}, sick_days:{},  kinda_sick: {}, hate_your_job: {}, call sick boolean : {}".format(
    actually_sick, sick_days, kinda_sick, hate_your_job,  calling_in_sick))

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#### test : not False ####
test_bool = 0
# test_bool = False
if not test_bool:
    print( "not test_bool : ")
else :
    print("...")

x = 1 #T
y = 1 #T
if not x or y:
    print('winter is coming')
else: 
    print('valar morghulis') 