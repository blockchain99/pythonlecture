'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''

# def mode(alist):
#     return max({alist.count(x)                  )

# print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])) # 4

print("------test1--list of duplicated dict-> woring approach-----")
test1 = [2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]
listdic= [{x:test1.count(x)} for x in test1] 
print(listdic)
                       

print("-----------------")

print("---nested value")
print([[v for k,v in e.items()]for e in listdic])
print("---nested value w/o []")
print([[v for k,v in e.items()][0]for e in listdic])
print("---nested key")
print([[k for k,v in e.items()]for e in listdic])
print("---nested key w/o []")
print([[k for k,v in e.items()][0]for e in listdic])
print("---nested key, value")
print([[(k,v) for k,v in e.items()]for e in listdic])
# print([((k,v) for k,v in e.items()) for e in listdic]) #generator object

print("++++++++++++++++test+++++++++++++++++++++")
test = [2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]
print(list(test.count(x) for x in test)) #list(count_obj)

keys = []
values =[]
for x in test:
   keys.append(x)
   values.append(test.count(x))
newdict = dict(zip(keys,values))
print("**dictionary : ",newdict)
maxnum = 0
for k,v in newdict.items():    
    # maxnum = 0 #alway initialized to 0 -> move outside of for loop
    print("******",k,v)
    if v > maxnum:
        maxnum = v
        print(f"maxnum is  {maxnum} key is {k}, value is {v}")
    

print("===--------test: frequency dict---------")
def CountFrequency(my_list): 
  
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
  
    for key, value in freq.items(): 
        print ("% d : % d"%(key, value))

my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2] 
CountFrequency(my_list)