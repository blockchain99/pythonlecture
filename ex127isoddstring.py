'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''
#sum of each charactoer's position is odd -> True 
print("-----------test--------------")
characters = ['a','b,','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z']
numbers = [x for x in range (1, 26)]
print(numbers)
dic_zip_char_num = dict(zip(characters, numbers))
print(dic_zip_char_num)

print("-----------==  ------")
def is_odd_string(astring):#A is index 1(not 0), "a" first position,"b" second
    return sum([ dic_zip_char_num[char] for char in astring]) % 2 == 1 

print(is_odd_string('a')) # True
print(is_odd_string('aaaa')) # False
print(is_odd_string('amazing')) # True
print(is_odd_string('veryfun')) # True
print(is_odd_string('veryfunny')) # False

print("--------test-------")
print(1+13+1+25+9+14+7)
print((1+13+1+25+9+14+7)%2 == 1) #False

print("---test-- string to number----")
def is_odd_string2(astring):#A is index 1(not 0), "a" first position,"b" second
    return ([ dic_zip_char_num[char] for char in astring])

print(is_odd_string2('a')) # True
print(is_odd_string2('aaaa')) # False
print(is_odd_string2('amazing')) # True
print(is_odd_string2('veryfun')) # True
print(is_odd_string2('veryfunny')) # False

print("----------lec------")
def is_odd_string3(string):
    total = sum((ord(c) - 96) for c in string.lower()) or 0 #very important!!
    return total % 2 == 1