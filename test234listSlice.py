mylist = list(range(0, 10)) #no incl last
print(len(mylist))
print(mylist)
print("--------------------")
print(mylist[-10]) #0
print(mylist[-9]) #-1
print(mylist[-10:0]) #-10 ~ -1 (0 not incl)
print("===============same index ====================")
print(list(range(-10, 0))) #last(0) not incl
print(list(range(0, 10))) #last(10) not incl

print("---------list with reverse index --------------")
print(mylist[-10:]) # [0:]
print(mylist[-9:])  # [1:]
print(mylist[-8:])
print("-----------------------------------------------")
print(list(range(-10, 0))) #last(0) not incl -10 ~ -1
print(mylist[:-10]) #last -10 not incl-> [0:0] -> blank item
print(mylist[:-9])
print(mylist[:-8])


