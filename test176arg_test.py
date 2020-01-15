def contains_purple(*args):
    if "purple" in args:
        return True
    return False

def combine_words(string, **kwargs):
    if "prefix" in kwargs:
        return kwargs['prefix']+string
    elif "suffix" in kwargs:
        return string+kwargs["suffix"]
    else:
        return string

print(combine_words("child"))
print(combine_words("child", prefix="man")) 
print(combine_words("child", suffix="ish"))
print(combine_words("work", suffix="er"))
print(combine_words("work", prefix="home"))


print("<high==========parameter ordering =====")
# prameter, *args, default parameter, **kwargs
#### args is tuple *args, 3 -> (3,) ###
def param_order(a,b,*args,instructor="Colt",**kwargs):
    return [a,b,args,instructor,kwargs]
print(param_order(1,2,3,last_name="Steele", job="Instructor"))

########### use * as an argument to a function to "unpack" values########
print("--------------------------")
def sum_all_values(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)

nums_list = [1,2,3,4,5]
nums_tuple =(1,2,3,4,5)
# sum_all_values(nums_list) #error :  int + list
# sum_all_values(nums_tuple) #error :  int + tuple

sum_all_values(1,2,3,40) 
sum_all_values(*nums_tuple)
print("*num_list----")
sum_all_values(*nums_list)

print("#############unpacking from tuple or list#########")
# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:
arglist = [1,4,7]
result1 = count_sevens(*arglist)
result11 = count_sevens((1,4,7))
print(result1)
result2 = count_sevens(*nums)
print(result2)

###########use ** as an argument:Dictionary unpacking######
def display_names(first, second):
    print(f"{first} says hello to {second}")

display_names(first="James", second="Tom") #must same as func parameter.

names = {"first": "Colt", "second":"Joshua"}
# display_names(names) #error: just 1 arg(dict itself) instead of 2 elements
display_names(**names) #unpacking dict

def add_and_multiply_numbers(a,b,c):
    return a + b * c
data = dict(a=1,b=2,c=3)
print(add_and_multiply_numbers(**data))

print("===++====")
def add_and_multiply_numbers1(a,b,c, **kwargs):
    print(a + b * c) 
    print("OTHER STUFF...")
    print(kwargs)
data = dict(a=1,b=2,c=3) #dic
add_and_multiply_numbers1(**data)

print("===++====2====")
def add_and_multiply_numbers2(a,b,c, **kwargs):
    print(a + b * c) 
    print("OTHER STUFF...")
    print(kwargs)
data = dict(a=1,b=2,c=3,d=55, name="Tome") #dic
add_and_multiply_numbers2(**data)

print("===++====3====")
def add_and_multiply_numbers3(a,b,c, **kwargs):
    print(a + b * c) 
    print("OTHER STUFF...")
    print(kwargs)
data = dict(a=1,b=2,c=3,d=55, name="Tome")
add_and_multiply_numbers3(**data, cat="blue")

# print("=====-----------calculate===dictionary ===")
# '''
# calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
# calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
# '''

# def calculate(make_float,operation,**kwargs): # **kwargs: flexible number of dic arguments.
    
#     if operation =='add':
#         if 'message' in kwargs.keys():
#             if make_float:
#                 return kwargs['message'] + float(kwargs['first'] + kwargs['second'])
#             return kwargs['message'] + int(kwargs['first'] + kwargs['second'])
#         else:
#             if make_float:
#                 return 'The result is ' + float(kwargs['first'] + kwargs['second'])
#             return 'The result is ' + int(kwargs['first'] + kwargs['second'])
#     if operation =='subtract':
#         if 'message' in kwargs.keys():
#             if make_float:
#                 return kwargs['message'] + float(kwargs['first'] - kwargs['second'])
#             return kwargs['message'] + int(kwargs['first'] - kwargs['second'])
#         else:
#             if make_float:
#                 return 'The result is ' + float(kwargs['first'] - kwargs['second'])
#             return 'The result is ' + int(kwargs['first'] - kwargs['second'])
#     if operation =='multiply':
#         if 'message' in kwargs.keys():
#             if make_float:
#                 return kwargs['message'] + float(kwargs['first'] * kwargs['second'])
#             return kwargs['message'] + int(kwargs['first'] * kwargs['second'])
#         else:
#             if make_float:
#                 return 'The result is ' + float(kwargs['first'] * kwargs['second'])
#             return 'The result is ' + int(kwargs['first'] * kwargs['second'])
#     if operation =='divide':
#         if 'message' in kwargs.keys():
#             if make_float:
#                 return kwargs['message'] + float(kwargs['first'] / kwargs['second'])
#             return kwargs['message'] + int(kwargs['first'] / kwargs['second'])
#         else:
#             if make_float:
#                 return 'The result is ' + float(kwargs['first'] / kwargs['second'])
#             return 'The result is ' + int(kwargs['first'] / kwargs['second'])
#     else:
#         return 'Input Error'

# print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"
# print(calculate(make_float=True, operation='divide', first=3.5, second=5)) # "The result is 0.7"

print("======dictionary create:{}, dict() ======")
dic={'msg':'love', 'name':'jone', 'age':20}
print(dic)

# dic3={msg:'love', name:'jone', age:20}#NameError: name 'msg' is not defined
# print(dic3)

# dic1 = dict('msg'='love', 'name'='jone', 'age'=20) #error: keyword can't be an expression 
dic1 = dict(msg='love', name='jone', age=20) 
print(dic1)

print(dic1['msg']) #love
print('string context '+str(2.3))



