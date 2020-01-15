'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''
vowl = ['a','e','i','o','u']
## in below dictionary all vowls intilized with o -> 
#  vowl not appreaed ->  0 in dictionary. 
# dictcount ={
#     'a':0,'e':0,'i':0,'o':0,'u':0
# }
dictcount = {}
print("----------vowl, dictcount is out of function -------")
def vowel_count(strlist):
    count = 0
    for char in strlist:
        if char in vowl:
            count += 1
            dictcount[char] = count
    return dictcount    
    


print(vowel_count('awesome')) # {'a': 1, 'e': 2, 'o': 1}
print(vowel_count('Elie')) # {'e': 2, 'i': 1}
print(vowel_count('Colt')) # {'o': 1}

print("----shor ver: from itertools import count----")
from itertools import count

def vowel_count1(strlist):
    for element in strlist:
        if element in vowl:
            dictcount[element] = strlist.count(element)
    return dictcount
    
print(vowel_count1('awesome')) # {'a': 1, 'e': 2, 'o': 1}
print(vowel_count1('Elie')) # {'e': 2, 'i': 1}
print(vowel_count1('Colt')) # {'o': 1}


print("---------lec --------")
def vowel_count2(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}
print("------test--------")
newdict = dict(a=2, b=3, c=9)
print(newdict)
newdict1 = {"a":2, "b":34, "xx":88}
print(newdict1)