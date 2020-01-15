'''
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''

print("----------test-----------")
vowls = 'aeiou' #strubg
def put_char(astring):
    return [x for x in astring] #list ['a', 'e', 'i', 'o', 'u']

print(put_char(vowls))
print("-same--", list(vowls)) #['a', 'e', 'i', 'o', 'u']

print("========test=vowl reverse with enumerate => Not good idea-> need to use Dictionary==")
def reverse_vowels1(astring):
    vowls = list('aeiou')
    vowl_in_str = [x for x in astring if x in vowls]
    all_key_val = [(i, val) for i, val in enumerate(astring)]
    vowl_from_all = [(i, val) for i, val in enumerate(astring)if val in vowls]
    vowl_from_all_rev = list(reversed(vowl_from_all))
    vowl_from_all_list = [[i, val] for i, val in enumerate(astring)if val in vowls]
    vowl_from_all_list_rev = list(reversed(vowl_from_all_list))
    print(vowl_in_str)
    print(len(vowl_in_str))
    print(all_key_val)
    print("* vowl_from_all",vowl_from_all)
    print("* vowl_from_all_list",vowl_from_all_list)
    print("* vowl_from_all_reverse",vowl_from_all_rev)
    print("* vowl_from_all_list_reverse",vowl_from_all_list_rev)
    # return if val in vowls for i, val in enumerate(astring)
# print(reverse_vowels1("Hello!") )# "Holle!" 
reverse_vowels1("Tomatoes") # "Temotaos" 
# print(reverse_vowels1("Reverse Vowels In A String") )# "RivArsI Vewols en e Streng"
# print(reverse_vowels1("aeiou") )# "uoiea"
# print(reverse_vowels1("why try, shy fly?") )# "why try, shy fly?"


print("-----enumerate reverse test----")
a = ["foo", "bar", "baz"]
# enu_a = [[i, val] for i, val in enumerate(a)]
enu_a = [[i, val] for i, val in enumerate(a)]
enu_a2 = list(enumerate(a))
print("enume rev: ", enu_a)
print("enume rev2 : ", enu_a2)

print("------listname.reverse() reversed(list_name)list---")
mylist = [1, 2, 3, 4, 5]
mylist.reverse()
print(mylist)
mylist2 = [1, 2, 3, 4, 5]
newrevlist  = list(reversed(mylist2))
print("* newrevlist", newrevlist)

vowls = list('aeiou')
vowls_rev = vowls[::-1]
print("---- pop test---")
ne = []
test1 = ['e', 'o']
# print(test1.pop())
ne.append(test1.pop())
print(ne)
print(test1)

print("=============using pop()==project=(if - elif )====correct!============")
def reverse_vowels2(astring):
    print(astring)
    astring = list(astring)
    print(astring)
    vowls = list('aeiou')
    print(vowls)
    print("--------")
    vowl_in_str = [x for x in astring if x in vowls]
    vowl_in_str_rev = list(reversed(vowl_in_str))
    print("*before: vowl_in_str:", vowl_in_str)
    # print(vowl_in_str_rev)
    newstr = []
    for x in astring:
        # if x in vowl_in_str:     #error since it is popped and changed -> vowls 
        ##not as intened!
        if x in vowls:   
            tobereplaced = vowl_in_str.pop()
            newstr.append(tobereplaced)
            print("* after: vowl_in_str: ", vowl_in_str)
        else:
            newstr.append(x)
        print("-newstr :",newstr)
    return ''.join(newstr)

# print(reverse_vowels2("Hello!") )# "Holle!" 
print(reverse_vowels2("Tomatoes")) # "Temotaos" 
# print(reverse_vowels2("Reverse Vowels In A String") )# "RivArsI Vewols en e Streng"
# print(reverse_vowels2("aeiou") )# "uoiea"
# print(reverse_vowels2("why try, shy fly?") )# "why try, shy fly?"

print("=============using pop()==project=(olny if  )====wrong!============")
def reverse_vowels3(astring):
    print(astring)
    astring = list(astring)
    print(astring)
    vowls = list('aeiou')
    print(vowls)
    print("--------")
    vowl_in_str = [x for x in astring if x in vowls]
    vowl_in_str_rev = list(reversed(vowl_in_str))
    print("*before: vowl_in_str:", vowl_in_str)
    # print(vowl_in_str_rev)
    newstr = []
    for x in astring:
        # if x in vowl_in_str:     #error since it is popped and changed -> vowls 
        ##not as intened!
        if x in vowls:   
            tobereplaced = vowl_in_str.pop()
            newstr.append(tobereplaced)
            print("* after: vowl_in_str: ", vowl_in_str)
        newstr.append(x)
        print("-newstr :",newstr)
    return ''.join(newstr)

# print(reverse_vowels3("Hello!") )# "Holle!" 
print(reverse_vowels3("Tomatoes")) # "Temotaos" 
# print(reverse_vowels3("Reverse Vowels In A String") )# "RivArsI Vewols en e Streng"
# print(reverse_vowels3("aeiou") )# "uoiea"
# print(reverse_vowels3("why try, shy fly?") )# "why try, shy fly?"

