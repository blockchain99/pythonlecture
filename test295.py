print(2*'a')
print('2' + '2')
# print('2' + 2) #error
# print(2 + 'a') #error
# print('a' + 2) #error
print("------------------")
try:
   print(2 + '2')
except TypeError as err:
    print(f"Error : {err}")
print("-------------===========")
def check():    
    try:
        return 2 + '2'  
    except TypeError as err:
        print(f"Error : {err}")

check()