def say_hello():
    instructor = 'Colt'
    return f'Hello {instructor}'

say_hello() #no print
print(say_hello())

# print(instructor) # NameError

print("--------------------------")
# total = 0
# def increment():
#     total += 1
#     return total
# increment() # Error!

## UnboundLocalError: local variable 'total' referenced before assignment
## Lets us reference variables that were originally assigned on the global scope

print("-------------============")
total1 = 0

def increment1():
    global total1
    total1 += 1
    return total1

increment1() # 1

print("===accessing not changed var in func-> OK ")
print("== but changed -> Error")
name ="Rusty"
def say():
    print(name)
say()

# def say1():
#     name += "!"
#     print(name)
# say1() #Error

## Just overwriting name="Rusty !" is OK
##If I need to manuplating var name in func -> global name

print("#######################")

def outer():
    """non local: modify a parent's var in a child(nested) func"""
    count = 0
    def inner():
        nonlocal count
        while(count < 10):
            count += 1
        return count
    return inner()
print(outer())

def say_h(): #""" ...""" can be shown func_name.__doc__
    """ simple function : comment """
    return "Hello !"
say_h.__doc__ # 'simple function : comment'

##########Show document of func, in command line $python3 ,, >> 
# >> import random
# >> random.randint.__doc__
# >> [1,2,3].pop.__doc__ 

def exponent(num, power=2):
    """ exponent(num, power) raises num to specified power.Power default is 2"""
    return num ** power

print(exponent(3, 4))
print(exponent(3))
print(exponent(7))

print(exponent.__doc__)
