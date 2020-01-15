print("======= dic version=======")
def return_day(number):
    switcher = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
    day = switcher.get(number) #return weekday.if not exit return None(False)
    # if day:
    #     return day
    # return None
    return day

print(return_day(3))
print(return_day(9))
print("======= list version=======")
def return_day1(number):
    weeklist=[ 
        "Sunday", #index 0
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "riday",
        "Saturday", #index 6
     ]
    # if number >= 0 and number <7:
    if number >= 0 and number <len(weeklist):
        day = weeklist[number]  #list has no mothod like .get(return None for not existing arg)
        return day
    return None
    # return day#IndexError: list index out of range

print(return_day1(6))
print(return_day1(7))
print(return_day1(9))

print("############ lec ver ##############")
def return_day1(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None

print("############ lec ver2 ##############")
# def return_day2(num):
#     return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]  
# print(return_day2(2)) # 1 for mon, 7 for sat
# print(return_day2(8)) #IndexError

print("------return_day3------")
def return_day3(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]  
    except IndexError as e:
        return None
print(return_day3(2)) # 1 for mon, 7 for sat
print(return_day3(8))

print("----------------------------------")

def last_element(alist):
    try:
        return alist[len(alist)-1]
        # return alist[-1]
    except IndexError as e:
        return None

print(last_element([1,2,3,4,5]))
print(last_element([]))

# def last_element2(alist):
#     return alist[len(alist)-1]
# print(last_element2([])) #IndexError
def last_element3(l): #lec ver
    if l:
        return l[-1]
    return None #if empty list, [] -> False
print(bool([]))

def number_compare(num1, num2):
    if num1 > num2:
        return "First is greater"
    elif num1 < num2:
        return "Second is greater"
    return "Numbers are equal"
print(number_compare(4, 9)) 

print("Hello World".lower().count("H".lower()))
print("Hello World".lower().count("U".lower()))

print(bool("H".lower() in "Hello World".lower())) #True

print("==================++")
def single_letter_count(st, w):
    if w in st:
        return st.lower().count(w.lower())
    return 0
print(single_letter_count("Hello World", "H"))
print(single_letter_count("Hello World", "k"))

print("-----multi letter count--------")
'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''
print("awesome".count('e'))
# flesh out multiple_letter count:
def multiple_letter_count(charlist):
    return { chr : charlist.count(chr) for chr in charlist}
print(multiple_letter_count("awesome"))

print("---------------------")
tl = [1,2,3]
popped = tl.pop()
print(popped)
print(tl)
tl.insert(1, 100) #insert before index 1
tl.insert(-1,200) #insert before the last(-1)
tl.insert(len(tl)-1,300) #insert before the last(-1)
tl.insert(len(tl), 500) #insert as last!!
print(f"**{tl}")
tl.pop(-1)
print(tl)
tl.pop(0)
print(tl)
print("++++++++++++some problem: if elif else ++++++++++++++")
'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

# def list_manipulation(alist, com, loc, val):
def list_manipulation(alist, com, loc, val=None): #val can not be here. 
    if com == "remove":
        if loc == "end":
            return alist.pop() #return removed value
            # return alist #return after popped
        elif loc == "beginning":
            return alist.pop(0) 
            # return alist
    elif com == "add":
        if loc == "beginning":
            alist.insert(0, val)
            return alist
        elif loc =="end":
            # alist.insert(len(alist), val) #insert before position
            alist.append(val)
            return alist

print(list_manipulation([1,2,3], "remove", "end") )# 3
print(list_manipulation([1,2,3], "remove", "beginning") )#  1
print(list_manipulation([1,2,3], "add", "beginning", 20)) #  [20,1,2,3]
print(list_manipulation([1,2,3], "add", "end", 30) )#  [1,2,3,30]
######## lec ver##############
def list_manipulation1(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection

print("-----------------------------")
'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''
tes = 'tacocat'
print(tes[-1])
print(tes[-2])
print(tes[-3])
print(tes[3])
print(tes[2])
print(tes[1])
print(tes[0])

print("======")
print(tes[len(tes)-1])

def is_palindrome(str):
    str = str.lower().replace(' ', '')
    isp = True
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-1-i]:
            isp =False
    return isp
print(is_palindrome('testing'))
print(is_palindrome('tacocat'))
print(is_palindrome('hannah'))
print(is_palindrome('amanaplanacanalpanama'))
print(is_palindrome('amaxaplanacanalpanama'))
print(is_palindrome('a man a plan a canal Panama'))

print("######## lec ver########")
def is_palindrome1(string):
    stripped = string.lower().replace(" ", "")
    return stripped == stripped[::-1]  #index 0 vs -1
print(is_palindrome1('testing'))
print(is_palindrome1('tacocat'))
print(is_palindrome1('hannah'))
print(is_palindrome1('amanaplanacanalpanama'))
print(is_palindrome1('amaxaplanacanalpanama'))
print(is_palindrome1('a man a plan a canal Panama'))

###########

def multiply_even_numbers(alist):
    tobe = filter(lambda x: x % 2 ==0, alist)
    # tobe = [ e for e in alist if e % 2 == 0]
    result = 1
    for e in tobe:
        result *= e
    return result
    
print(multiply_even_numbers([2,3,4,5,6]) )# 48

print([v for v in range(1, 10) if v % 2 ==0 ])

from functools import reduce
def reduce_mul_even(alist):
    tobe = filter(lambda x: x % 2 ==0, alist)
    return reduce(lambda a,b: a*b, tobe)
print(f"==reduce multiply even number=== \
  {multiply_even_numbers([2,3,4,5,6])}==" )# 48

'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(astr):
    return astr[0].upper()+astr[1:]
    # return astr[:1].upper() + astr[1:] #lec ver
   
print(capitalize("tim") ) 

print("###########--1111-------------------")
def compact(alist):
    """compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]"""
    return [li for li in alist if bool(li) != False
    # return [li for li in alist if li != False  #wrong outcome !!
    ]
    # return [li for li in alist if bool(li) == True] #same as 
    

    
print(compact([0,1,2,"",[], False, {}, None, "All done"]))
print("bool(None)==False: ",bool(None)==False)
print("None == False: ",None == False)
print(bool('')==False)
print(''==False)
print({}==False)
print("============= 2222==========")
def compact1(l): #lec ver
    return [val for val in l if val]
print(compact([0,1,2,"",[], False, {}, None, "All done"]))
print("bool(None)==False: ",bool(None)==False)
print("None == False: ",None == False)
print(bool('')==False)
print(''==False)
print({}==False)

print("test==========")
if not{} :
    print("{} is Falsy")
if not'':
    print("'' is Falsy")
if not"":
    print('"" is Falsy')
if not 0 :
    print("0 is Falsy")
if not[] :
    print("[] is Falsy")

print("========intersection list====")
def intersect(l1, l2):
        return [val for val in l1 if val in l2]
print(intersect([1,2,3,4], [3,4,5,6]))

def intersection1(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common
print("============= partition===========")
"""
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]

"""
def isEven(num):  #return True or False 
    return num % 2 == 0 

def partition(alist, fn):
        # truthy_list = filter(fn , alist) # filter obj,just use this, falsy_list wrong!
        truthy_list = list(filter(fn , alist)) # list
        # print([v for v in truthy_list])
        falsy_list = [x for x in alist if x not in truthy_list]
        # print([v1 for v1 in falsy_list])
        return [truthy_list, falsy_list]

print(partition([1,2,3,4], isEven))
# ===========lec ver1==========
def partition1(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]

#================lec ver2==========
def partition2(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]


a = range(1, 10)
print(type(a))
print(a)
print(list(a))
print("------range------")
b = set(range(10))
print(type(a))
print(a)
print("**************")
# a = list(range(1, 10))
a = range(1, 10) #same result above
print([x for x in a if x not in [2, 3, 7]])
# [1, 4, 5, 6, 8, 9]

print("##############set - for not repeating elements")
# If you don't have repeated values, you could use set difference.

x = set(range(10))
y = x - set([2, 3, 7])
print(y)
# y = set([0, 1, 4, 5, 6, 8, 9])

# =========================test============
a = range(1,50000) # Source list
b = range(1,15000) # Items to remove

def comprehension(a, b):
     return [x for x in a if x not in b]

def filter_function(a, b):
    return filter(lambda x: x not in b, a)

def modification(a,b):
    for x in b:
        try:
            a.remove(x)
        except ValueError:
            pass
    return a

def set_approach(a,b): #fastest
    return list(set(a)-set(b))