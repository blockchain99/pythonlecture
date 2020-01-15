#  if x is falsy or y is falsy, print "winter.. ", 
# otherwise print "valar..-> Incorrect !"

x = 0 #F
y = None #F
if not x or y:
    print('winter is coming')
else: 
    print('valar morghulis') 

# x: F, y:T -> otherwise. 

x = 1 #T
y = None #F
if not x or y:
    print('winter is coming')
else: 
    print('valar morghulis') 

x = 0 #F
y = 1 #T
if not x or y:
    print('winter is coming')
else: 
    print('valar morghulis') 

x = 1 #T
y = 1 #T
if not x or y:
    print('winter is coming')
else: 
    print('valar morghulis') 

print("#######set x to True, then sets x to False. ########")    
print("#######set x to True, then sets x to False, then set x to True-> Wrong###")    
x = True
if x:
    x = False
    print(bool(x))
 
elif not x:
    x = True
    print(bool(x))

#############################################
y= False 
if y:
    y = False
    print(bool(y))
 
elif not y:
    y = True
    print(bool(y))
    