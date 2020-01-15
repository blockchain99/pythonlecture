x = 15 
y = 0 #False
print (x or y) # 15
print (bool(x or y)) #True

x = 0
y = None
print (bool(x or y)) #False

x = 0
y = -1
print(bool(x or y and x - 1 == y and y + 1 == x))
# False or True -> True 
#True and True -> True 
#True and True-> True