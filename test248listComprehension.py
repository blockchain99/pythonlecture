suits = ["Hearts", "Diamonds", "Clubs","Spades"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

card = [ print(value, suit) for suit in suits for value in values]
print("-------------")
[ print(f"{value} of {suit}") for suit in suits for value in values]
print("-------------")
print(card)


print("--------min([a,b])--------")
#TypeError: 'builtin_function_or_method' object is not subscriptable
# print(min[23,33]) #TypeError
test = [1,2,3,4,5,6]
## 2 items removed 
print(test[-2:]) 
print("====result of remove 3 element from the last==")
print(test[:-3])
remove_num = input("How many numbers removed from list?")
print(test[:-int(remove_num)]) #list after remove 
