#This wrapper function simply runs the function, 
# and returns a list containing the result twice:

from functools import wraps
 
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper

@double_return 
def add(x, y):
    return x + y
    
print(add(1, 2)) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

print(greet("Colt")) # ["Hi, I'm Colt", "Hi, I'm Colt"] 