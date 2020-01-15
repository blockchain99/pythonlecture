# Decorators, which is function wrap other functions and enhance their behavior
# Decorators are examples of higher order functions
# Decorators have their own syntax, using "@" (syntactic suga

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

def greet():
    print("My name is Colt.")

def rage():
	print("I HATE YOU!")

# we are decorating our function 
# with politeness!
polite_greet = be_polite(greet)
polite_greet()
print("-----------------------------------")
polite_rage = be_polite(rage)
polite_rage()
print("---------2 with @be_polite1--------")
def be_polite1(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite1
def greet1():
    print("My name is Matt.")

@be_polite1
def rage1():
    print("I hate you")

# be_polite1(greet1()) #same as greet1()
greet1()
rage1()
# we don't need to set 
# greet1 = be_polite1(greet)1
# greet1()

print("##############shout###(one arg)##################")
def shout(fn):
    def wrapper(name):
        # return fn(name).upper()
        print( fn(name).upper() )
    return wrapper

@shout
def greet_shout(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side): #shout is one arg only, so order not excuted!!
    return f"Hi, I'd like the {main}, with a side of {side}, please."

# shout(greet_shout("Jone"))
greet_shout("Jone")
# print(shout(greet_shout("Jone")))

print("---------Decorator pattern ------------")
# def my_decorator(fn):
#     def wrapper(*args, **kwargs):
#         # do some stuff with fn(*args, **kwargs)
#         pass
#     return wrapper

print("--------log_function_data-(multi args)------")
def log_function_data(fn):
    def wrapper(*args, **kwargs):
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        print(fn(*args, **kwargs))
    return wrapper

@log_function_data
def add(x,y):
    '''Adds two numbers together.'''
    return x + y

@log_function_data
def cubic(x,y,z):
    '''multiply three numbers together.'''
    return x * y * z
log_function_data(add(1,3))
add(1,3) #same as above
log_function_data(cubic(2,3,4))
cubic(2,3,4)
print("---")
# print(add.__doc__)
# print(add.__name__)
# help(add)

print("###########Decorator pattern###########")
from functools import wraps
# wraps preserves a function's metadata
# when it is decorated
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print("------------------------------------")
        print(f"function name is {fn.__name__}")
        print(f"this is for {fn.__doc__}")
        print(f"total time elapsed is {end - start}")
        # print(f" the result of function excution is {result}")
        return f"the result of function excution is {result}"
    return wrapper

@speed_test
def sum_num_gen():
    ''' generator sum '''
    return sum( x for x in range(90000000))

@speed_test
def sum_num_list():
    ''' list sum '''
    return sum([x for x in range(90000000)])
print(sum_num_gen())
print(sum_num_list())