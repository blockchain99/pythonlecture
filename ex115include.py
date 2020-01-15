'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''

#accepts collection(string, list, dict), a value, optional starting index:
# True if include from starting index. otherwise False.
#1. string, array: third parameter is a starting index for where to search from.
#2. dictionary : search for value among value in dict.(3rd param ignored)

def includes(collects, val, start_index = None):  # w/o * before start_index -> error
    if type(collects) == list:
        if start_index:
            if val in collects[start_index:]:
                return True
            return False
        else:
            if val in collects:
                return True
            return False

    elif type(collects) == dict:
        if val in collects.values():
            return True
        return False

    else:
        if start_index:
            if val in collects[start_index:]:
                return True
            return False
        else:
            if val in collects:
                return True
            return False

#shift + alt + below arrow to choose multiple cursor
print(includes([1, 2, 3], 1)) # True 
print(includes([1, 2, 3], 1, 2)) # False 
print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False

print("--------simplify to remove duplicated logic-------")
def includes1(collects, val, start_index = None):  # w/o * before start_index -> error
    if type(collects) == dict:

        # return val in collects.values(): #just one line for below 2 lines

        if val in collects.values():
            return True
        return False

    else: #list and string is same logic
        if start_index:
            if val in collects[start_index:]: 
                return True
            return False
        else:
            if val in collects:
                return True
            return False

#shift + alt + below arrow to choose multiple cursor
print(includes1([1, 2, 3], 1)) # True 
print(includes1([1, 2, 3], 1, 2)) # False 
print(includes1({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes1({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes1('abcd', 'b')) # True
print(includes1('abcd', 'e')) # False

print("---------3rd ----args[2]-> IndexError -> len(args) ==3 ------")
# (collects, val, start_index = None)
def includes2(*args):  #w/o * before start_index -> error
  
    if type(args[0]) == dict:
        if args[1] in args[0].values():
            return True
        return False

    # else:
    #     if args[2]: #may cause IndexError
    #         if args[1] in args[0][args[2]:]:
    #             return True
    #         return False
    #     else:
    #         if args[1] in args[0]:
    #             return True
    #         return False

    else: #check len(args) == 3 -> start_index exist. else None
        if len(args) == 3:
            if args[1] in args[0][args[2]:]:
                return True
            return False
        else:
            if args[1] in args[0]:
                return True
            return False

print(includes2([1, 2, 3], 1)) # True 
print(includes2([1, 2, 3], 1, 2)) # False 
print(includes2({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes2({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes2('abcd', 'b')) # True
print(includes2('abcd', 'e')) # False


print("------ lec ------")
def includes3(item,val,start=None):
    if type(item) == dict:
        return val in item.values()
    if start is None:
        return val in item
    return val in item[start:]

print("-------test----------")
tst = 'abcd'
print('a' in tst) #T
print('a' in tst[1]) #F