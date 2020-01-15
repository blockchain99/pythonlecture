#accept two list of varing lengh, one is key the other is value -> make dict
#not enough value(key_num > val_num) -> null value,not enough key -> just ignore ramining value.

'''
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
'''
print('-------dictionary.get("key") -> return None if not exist ----')
def two_list_dictionary(keys, values):
# # #incorrect  when number of (key list, value list) is not matched.
#     # new_dict = dict(zip(keys, values)) 
#     # return new_dict

#     # return {  keys[i] : values[i] for i in range(0, len(keys))} #IndexError

##origin_dict.update(other_dict) :adds element(s) to the dictionary if the key 
# is not in the dictionary. 
# If the key is in the dictionary, it updates 
# the key with the new value.  -> origin dict is updated
# It doesn't return any value (returns None).  
    if len(keys) > len(values): #not enough value-> remaing value to None
        origin_dict = {}.fromkeys(keys, None)
        print("--",origin_dict)
        other_dict = dict(zip(keys, values))
        print("**",other_dict)
        origin_dict.update(other_dict)
        return origin_dict
    return {keys[i] : values[i] for i in range(0, (len(keys)))}    
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4])) # {'a': 1, 'b': 2, 'c': 3}
print(two_list_dictionary(['x', 'y', 'z']  , [1,2])) # {'x': 1, 'y': 2, 'z': None}

print("----------test-----------")
answer = dict.fromkeys("aeiou", 0)
print(answer)
answer1= {}.fromkeys(['a','e','i','o','u'], 0)
print(answer1)

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
answer3 = {list1[i]: list2[i] for i in range(0,3)}
print(answer3)

print("-------test--zip with cycle----")
from itertools import cycle 
  
# Initialising list of dictionary 
ini_lis1 = ['a', 'b', 'c', 'd', 'e'] 
ini_lis2 = [1, 2, 3] 
  
# zipping in cyclic if shorter length 
result = {v: ini_lis2[i % len(ini_lis2)]  
          for i, v in enumerate(ini_lis1)} 
  
print("resultant dictionary : ", str(result)) 

print("----dict.get('key')---if not exit -> None-----")
dic = {"A":1, "B":2} 
print(dic.get("A")) #1
print(dic.get("C")) #None
print(dic.get("C","Not Found ! ")) 

print("----- test -origin_dict.update(other_dict)-> origin_dict is updated------")
adict = {'x': None, 'y': None, 'z': None}
bdict = {'x': 1, 'y': 2}
adict.update(bdict)
print(adict) #{'x': 1, 'y': 2, 'z': None} It works !!
c = adict.update(bdict) 
print(c) #None