# import random #import everything as an attribute random
# print(random.randint(1,5))

import random as my_rd
print(my_rd.random()*10)
print(my_rd.randrange(2,11,2)) #random even number from2 to 10

# import random 
# print(randint(1,5)) #NameError: name 'randint' is not defined

from random import * #import everything to current name space
print(randint(1,5))


