list1=["hello"]
# list1[2] #IndexError
colors =["yellow", "green", "blue", "black","red"]
def colorize(text, color):
    if type(text) is not str:
        raise TypeError("text must be string") #my own error message.
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")

colorize('mybook', 'yellow')
# colorize(41, 'yellow') #TypeError: Text must be string.
# colorize('mybook', 'purple') #Value: color is invalid color

def get(d, key): #dic , key
    try:
        return d[key]
    except KeyError:
        return None

d = {'name' : "Ricky"}
# print(get(d,'name'))
print(get(d,'city'))#KeyError -> None

print("------try except catch finally----")
while True:
    try:
        num = int(input("Input the number:"))
    except:
        print("It's not number!")
    else:
        print("Good you entered number!")
        break
    finally:
        print("Runs no matter what.")
print("Rest of game logic runs!")
print("===---===--")
def divide(a,b):
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
print(divide(1,2))
print(divide(1,0))
print(divide(1,'a'))

print("--------TypeError----------")
def add(a,b):
  return a+b
 
#TypeError: add() missing 1 required positional argument: 'b' 
# add(1)

# sum = 4 + "4" #TypeError

########################################################
# A TypeError occurs when an operation or function 
# is applied to an object of inappropriate type.
#ex. int type has no len()

# A ValueError occurs when a built-in operation or function 
# receives an argument that has the right type 
# but an inappropriate value, and the situation 
# is not described by a more precise exception such as IndexError.

# len(42)    # this causes a TypeError, because a number is the wrong type for the function
#TypeError: object of type 'int' has no len()
# 4 + '4' #TypeError

# int("dog") # this causes a ValueError, because "dog" cannot be converted to an int value
#ValueError: invalid literal for int() with base 10: 'dog'

print(type("dog")) #class 'str'
print(type(20)) #class 'int'
