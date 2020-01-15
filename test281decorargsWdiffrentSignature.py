# This version only accepts one argument
# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

# This version works with any number of args
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def greet2(name, weight):
    return f"Hello {name}, your weight is {weight}"

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

@shout
def order2(main, side, drink):
    return f"Hi, I'll have {main}, with a side of {side}, and {drink}."

@shout
def lol():
	return "lol"

print(greet("todd"))  #  *args (one arg -> list)
print(greet2("James", 200))
print(order(side="burger", main="fries")) # **kwargs (two dict)
print(order2(side="burger", main="fries", drink="coke")) # **kwargs (two dict)
print(lol()) # no arg -> list