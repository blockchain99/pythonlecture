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
    # print(switcher.get(argument, "Invalid month")) 
    print(f"** without 2nd arg: {switcher.get(argument)}") 

# switch_demo(13)
print(f"print(func_name) : {switch_demo(13)}")

print("===============None is False=============")
print(f"***{bool(None)}")
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

def speak(animal = "dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal) #return sound if not exit-> None (False)
    if noise:
        return noise
    return "?"

print(speak("cat"))

print(speak())