'''
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''
print("--------not intended ---------")
def find_the_duplicate(alist):
    return list(x if alist.count(x) > 1 else None for x in alist) #not as intended!
    
print(find_the_duplicate([1,2,1,4,3,12])) # 1
print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
print(find_the_duplicate([2,1,3,4])) # None

print("------------2nd --dictionary with key: count of key----------")
def find_the_duplicate1(alist):
    result_dict = {num: alist.count(num) for num in alist}
    return result_dict


print(find_the_duplicate1([1,2,1,4,3,12])) # 1
print(find_the_duplicate1([6,1,9,5,3,4,9])) # 
print(find_the_duplicate1([2,1,3,4])) # None

print("------------3rd -----OK-------")
def find_the_duplicate3(alist):
    check_temp = []
    for e in alist:
        if e in check_temp:
            return e
        check_temp.append(e)
    return None
print(find_the_duplicate3([1,2,1,4,3,12])) # 1
print(find_the_duplicate3([6,1,9,5,3,4,9])) # 
print(find_the_duplicate3([2,1,3,4])) # None

print("--------lec-----")
def find_the_duplicate4(arr):
    counter = {}
    for val in arr:
        if val in counter:
            counter[val] += 1
        else:
            counter[val] = 1
    for key in counter.keys():
        if counter[key] > 1:
            return int(key)

print("-----test- one line with map and filter-----")
names = [
    {'first':'Rusty', 'last': 'Steele'}, 
    {'first':'Colt', 'last': 'Steele', }, 
    {'first':'Blue', 'last': 'Steele', }
]
print("*first key, value in names dictionayr:",names[0].items())

print("**** if list, names 's element is less than 5 then, print each element.**")
comb2 = list(map(lambda x: f"Your instructor is {x}",filter(lambda x: len(x) < 5, names)))
print(comb2)

# print("-- if length of first(such as 'Rusty') dictionary element is less than 5, then print ")
# comb3 = list(map(lambda x: f"Your instructor is {x}",filter(lambda x : len(x[0]) < 5, names)))
# print(f"---updated : {comb3}" )

print(list(map(lambda x : x.items(), names)))
# print(map(lambda x : x.items(), names)) #map obj

print("==========sort based on dict value -------sorted")
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(x)
print("** value based sort** operator.itemgetter(1)")
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(sorted_x)
sorted_x_rev = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_x_rev)
print("** key based sort** operator.itemgetter(0)")
sorted_x1 = sorted(x.items(), key=operator.itemgetter(0))
print(sorted_x1)
sorted_x_rev1 = sorted(x.items(), key=operator.itemgetter(0), reverse=True)
print(sorted_x_rev1)
print("--- dict output--OrderedDict(..)-")
import collections

sorted_dict = collections.OrderedDict(sorted_x)
print(sorted_dict)