#we dont't need to define our own __init__(),
#we can instead use the exsing dict __init__()

class GrumpyDict(dict): #no need to difine __init__() snice no property,attribute
    def __repr__(self):
        # return "NONE OF YOUR BUSINESS"
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()  #super() class -> dict : so show as dictionary form.

    def __missing__(self, key): #built-in if key is not in dict using 
        return f"{key} is not in dict"

    def __setitem__(self, key, value):
        print("you want to change the dictionary?")
        print("OK, Fine..")
        # super().__setitem__(key, value)
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("NO It aint here")
        return False
       
       
data = GrumpyDict({"first":"Tom", "animal":"cat"})
print(data)

print(data['city']) #instead of call function, use dictionary form.

print("--=------")
data['city'] = 'Tokyo'
print(data)

print("====------------")
print(data)
print('city' in data)
print('seoul' in data)

# >>> my_list = ["a", "b", "c"]
#     >>> my_list.__contains__("a")
#     True
#     >>> "a" in my_list
#     True