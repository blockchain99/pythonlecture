'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''
print("--remove only first second element--")
def remove_every_other(alist):
    if len(alist) > 1:
        alist.pop(1) #second element in list
        return alist #original list except popped second element. 
    return alist

print(remove_every_other([1,2,3,4,5])) # [1,3,5] 
print(remove_every_other([5,1,2,4,1])) # [5,2,1]
print(remove_every_other([1])) # [1] 

print("------lec---(remove all every other element-----")
def remove_every_other1(lst):
    return [val for i,val in enumerate(lst) if i % 2 == 0]