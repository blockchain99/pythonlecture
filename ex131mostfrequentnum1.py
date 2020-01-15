'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''
print("----------using dictionary------------")
def mode(alist):
    keys = []
    values =[]
    for x in alist:
        keys.append(x)
        values.append(alist.count(x))
    newdict = dict(zip(keys,values)) #{2: 2, 4: 7, 1: 1, 3: 2, 5: 1, 6: 2, 7: 1}
    # return(newdict)
    maxval = max([v for k,v in newdict.items()])
    print("*max value's index:",maxval)
    return [k for k,v in newdict.items() if v == maxval][0]

#option 2 --lec ver :  index of values list with max val -> find index of keys list
    # correct_index = list(newdict.values()).index(maxval) #4:7 is index 1(2nd element)
    # print(correct_index)
    # return list(newdict.keys())[correct_index] 
test = [2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]
print(mode(test))


print("-------lec -------")
def mode1(collection):
    count = {val: collection.count(val) for val in collection}
    # find the highest value (the most frequent number)
    max_value = max(count.values())
    # now we need to see at which index the highest value is at
    correct_index = list(count.values()).index(max_value)
    # finally, return the correct key for the correct index (we have to convert cou)
    return list(count.keys())[correct_index]

    