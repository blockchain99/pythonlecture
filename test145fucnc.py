def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False

def is_odd_number1(num):
    if num % 2 != 0:
        return True
    else:
        return False
testn = {is_odd_number(x) for x in range(1, 12)} #set -> not this case 
testnlist=[is_odd_number(x) for x in range(1, 12)] #list : correct
testdict = {x: is_odd_number1(x) for x in range(1, 12)} #dict 
print(testn)
print(f"** without list before range:{[is_odd_number(x) for x in list(range(1, 12))]}")#list : correct
print(testnlist)
print(testdict)
 #############################################
fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
even = filter(lambda x: x % 2 == 0, fibonacci)  
odd_numbers = list(filter(lambda x: x % 2, fibonacci)) # x%2 -> 1 -> T
print(list(even))
print("###########******########################")

# print(list(filter(lambda x: x % 2 == 0 for x in range(1, 50)))) #error
print(filter(lambda x: x % 2 == 0, range(1, 50)))
print(list(filter(lambda x: x % 2 == 0, range(1, 50))))
print( [x for x in range(1,50) if x%2 == 0] )
def generate_events():
    return [v for v in range(1, 50) if v % 2 ==0]
def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result

def yell(strin):
    return strin.upper()
print(yell("go away"))

print("##### else is not needed ####")
def is_odd(x):
    if x % 2 ==0 :
        return True #return exit func
    # else:
    #     return False
    return False
print(is_odd(9))
print(is_odd(4))

def exponent(num, power=2): #default is power=2 (if power not specified, 2)
	return num ** power

print(exponent(2,3)) #8
print(exponent(3)) #9
print(exponent(7)) #49
print("------------ default param-------")
def add(a =10, b=20):
    return a+b 
print(add())

print("--------default param is func---")
def add(a,b):
    return a+b
def math(a, b, fn=add):
    return fn(a,b)
def subtract(a,b):
    return a-b
print(math(2,3))
print(math(2,2, subtract))

print("======switcher dictionary mapping ====")
def switch_demo(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print(switcher.get(argument, "Invalid month"))
print(switch_demo(2))

def speak(animal="dog"):#default parameter,animal (assigned to "dog")
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal) #get: return sound if not exit -> return none(False)
    if noise: 
        return noise
    return "?"
    
def speak1(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')

def speak2(animal="dog"): #default parameter,animal (assigned to "dog")
    if animal == "pig":
        return "oink"
    elif animal == "duck":
         return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"

print(speak("cat")) #call function, speak with argument, "cat"