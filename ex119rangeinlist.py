'''
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
'''
#return sum of values btween(and including) start, end index
# 1. slice with star, end
# 2 then sum all sliced lists with sum()

from functools import reduce
# def range_in_list(alist, start=None, end=None): 
#     return sum(alist[start:end+1]) #None + 1 : TypeError

# def range_in_list(alist, *args):
#     return sum(alist[args[0]:args[1]]) #IndexError: tuple index out of range

# # def range_in_list(alist, start=None, end=None): 
# #     return reduce(lambda x,y : x+y , alist[start:end+1]) #None + 1 -> error

# # def range_in_list(*arg): 
# #     #IndexError: tuple index out of range
# #     return reduce(lambda x,y : x+y , arg[0][arg[1]:arg[2]]) #None + 1 -> error

def range_in_list(*args):
    if len(args) == 3:
        return sum(args[0][args[1]: args[2]+1])  #end index including -> need one more
    elif len(args) ==2:
        return sum(args[0][args[1]:])
    elif len(args) == 1:
        return sum(args[0])

print(range_in_list([1,2,3,4],0,2)) #  6
print(range_in_list([1,2,3,4],0,3)) # 10
print(range_in_list([1,2,3,4],1) )#  9
print(range_in_list([1,2,3,4]) )# 10
print(range_in_list([1,2,3,4],0,100)) # 10
print(range_in_list([],0,1)) # 0

print("------------lec----------")
def range_in_list1(lst, start=0, end=None):
    end = end or lst[-1]  #hard to get it
    return sum(lst[start:end+1])


print("------- test--reduce- from functools import reduce-----")
from functools import reduce
tl = [1,2,3,4,5,6]
result = reduce(lambda x,y : x+y, tl)
print("***all sum",result)
result14 = reduce(lambda x,y : x+y, tl[1:4]) #index 1,2 ,3 => 9
print("--start 1, end 4--",result14)

print(sum(tl))

#sum(iterable, 10) #10 + then element of list: 
print(sum(tl, 10)) #10 + sum of list

# # print(None+1)  #error
# # print(''+1)

print("------ slice with end, which is larger the size of list--")
a= [1,2,3,4]
print(a[1:6])  #just 2,3,4