from random import choice
listtest = [1,23,3,4,90]
print(choice(range(0,len(listtest))))
even = [x for x in range(0,10,2)]
print(even)

import numpy as np 
nprandint = np.random.randint(1,8, size=(2,3))
print(nprandint)