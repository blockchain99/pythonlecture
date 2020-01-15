'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''
#accepts a list and returs True if each value in a list is a list. 
#Otherwise, False.

def list_check(*args):    #correct !! 
    flag = True
    for arg in args:
        for x in arg: #input is nested list
            print("*",x)
            if type(x) != list:
                flag = False #Just one False makes result as False
    return flag

# def list_check(*args):
#     return all([[type(x) == list for x in li]for li in args])  #not as intented -> wrong !!
print(list_check([[],[1],[2,3], (1,2)])) # False : input is nested list -> need 2 for loops to access element
print(list_check([1, True, [],[1],[2,3]])) # False
print(list_check([[],[1],[2,3]])) # True

print("================= args for loop test==============")
def for_args(*args):
    for arg in args:
        print(arg)  #Just return one list consists of all list element ex) [[], [1], [2, 3], (1, 2)]
        if type(arg) == list:
            return True
        False
print(for_args([[],[1],[2,3], (1,2)])) 
print(for_args([1, True, [],[1],[2,3]])) # 
print(for_args([[],[1],[2,3]])) # 
print("----------- *data------------")
data1 = [[],[1],[2,3], (1,2)]
data2 = [1, True, [],[1],[2,3]]
data3 = [[],[1],[2,3]]
print(for_args(*data1)) 
print(for_args(*data2)) # 
print(for_args(*data3)) # 
print ("--------list check with list comprehension ->wrong: not as intened---")
def list_check2(*args):    #correct !! 
    # flag = True
    # for arg in args:
    #     for x in arg: #input is nested list
    #         print("*",x)
    #         if type(x) != list:
    #             flag = False #Just one False makes result as False
    # return flag

    return all([[type(x) == list for x in arg]for arg in args]) #not correct

    # return all(type(x) == list for x in args)  #not correct!

print(list_check2([[],[1],[2,3], (1,2)])) # False
print(list_check2([1, True, [],[1],[2,3]])) # False
print(list_check2([[],[1],[2,3]])) # True

print("-----lec ver!!---not using list ---")
def list_check_lec(vals):
    return all(type(l) == list for l in vals)
print(list_check_lec([[],[1],[2,3], (1,2)])) # False
print(list_check_lec([1, True, [],[1],[2,3]])) # False
print(list_check_lec([[],[1],[2,3]])) # True

print("------- test --- list comprehension - multi for loop--")
# uppers =  [[x.upper() for x in row]for row in csv_reader] # reader obj -> list

print("---------------------test1 ** correct!!")
# test_list = [[],[1],[2,3], (1,2)]
# test_list = [[],[1],[2,3]]
test_list = [1, True, [],[1],[2,3]]
for alist in test_list:
    print(alist)
    if type(alist) == list:
        print ("yes list type ")
    else:
        print("no")
    print("===")
print("---------------------test11**correct !!")
test_list1 = [[],[1],[2,3], (1,2)]
test_list3 = [1, True, [],[1],[2,3]]
test_list2 = [[],[1],[2,3]]

print(all([type(arg) == list for arg in test_list1])) 
print(all([type(arg) == list for arg in test_list2]))
print(all([type(arg) == list for arg in test_list3]))

print("------all(iterable)-----test2")
# all values true
l = [1, 3, 4, 5]
print(all(l))

# all values false
l = [0, False]
print(all(l))

# one false value
l = [1, 3, 4, 0]
print(all(l))

# one true value
l = [0, False, 5]
print(all(l))

# empty iterable
l = []
print(all(l))

print("----------- any(iterable)------------")
print(any([10, "", "one"])) 

gen = (i for i in [5, 0, 0.0, 4]) # generator
print(any(gen)) #True