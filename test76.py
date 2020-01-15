from random import randint
a = randint(0,2) #2 is included!!
print(a)

print("------np.random.randint------")
import numpy as np
print(np.random.randint(2, size=10)) #2 is not incl. 
##in vscode, ModuleNotFoundError: No module named 'numpy'  
## but this code in jupyter notebook : it works!!