'''
two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''
##list.sort(), list.sort(reverse = True)
def two_oldest_ages(alist): #two highest numbers in the list(incremental order)
    alist.sort()  # list with original name is sorted
    # return alist  #original list is sorted !!
    # return alist[-2:-1] #-8 (last -1 inddex -> not incl): wrong!
    return alist[-2:]


print(two_oldest_ages( [1, 2, 10, 8] )) # [8, 10]
print(two_oldest_ages( [6,1,9,10,4] )) # [9,10]
print(two_oldest_ages( [4,25,3,20,19,5] )) # [20,25]