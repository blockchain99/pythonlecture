# Write a function called divide, which accepts two parameters 
# (you can call them num1 and num2). The function should 
# return the result of num1 divided by num2. 
# If you do not pass the correct amount of arguments to the function, 
# it should return the string "Please provide two integers or floats". 
# If you pass as the second argument a 0, Python will 
# raise a ZeroDivisionError, so if this function is invoked with 
# a 0 as the value of num2, return the string 
# "Please do not divide by zero"

    # Examples
    
    # divide(4,2)  2
    # divide([],"1")  "Please provide two integers or floats"
    # divide(1,0)  "Please do not divide by zero"

def divide(num1, num2): #my ver
    if num2 == '':
        raise TypeError("Please provide two integers or floats")
    if num2 == 0:
        raise ZeroDivisionError
    # try:
    #     result = num1/num2
    # except TypeError as err:
    #     print(err)
    result = num1/num2
    print(f"Divide {num1} by {num2} is {result}.")

def divide1(a,b): # lec ver
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total

divide1(2,8)
divide1(2)
# divide1(2,0)

#+++++++ ref +++++++
def colorize1(text, color):
    if type(text) is not str:
        raise TypeError("text must be string") #my own error message.
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")

colorize1('mybook', 'yellow')

#---------ref2------------
def divide2(a,b):
    try:
        result = a/b
    
    # except (ZeroDivisionError, TypeError) as err:
    #     print("Someting wrong!")
    #     print(err)

    except ZeroDivisionError:
        print("Don't divide by zero!!")
    except TypeError as err:
        print("a,b must be ints or floats")
        print(err)
    else:
        print(f"{a} divide by {b} is {result}")