'''
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''


print("=============using pop()==project=(if - elif )====correct!============")
def reverse_vowels2(astring):
    print("=======================start here=================")
    print(astring)
    astring = list(astring)
    print(astring)
    # vowls = list('aeiou')
    vowls1 = list('aeiouAEIOU')
    # print(vowls)
    print(vowls1)
    print("--------")
    # vowl_in_str = [x for x in astring if x in vowls]
    vowl_in_str = [x for x in astring if x in vowls1]
    vowl_in_str_rev = list(reversed(vowl_in_str))
    print("*before: vowl_in_str:", vowl_in_str)
    # print(vowl_in_str_rev)
    newstr = []
    for x in astring:
        # if x in vowl_in_str:     #error since it is popped and changed -> vowls 
        ##not as intened!
        # if x in vowls:   
        if x in vowls1:    ###spooky if else !!
            tobereplaced = vowl_in_str.pop()
            newstr.append(tobereplaced)
            # print("* after: vowl_in_str: ", vowl_in_str)
        else:  #W/O this else then go forward below line-> wrong results!
            newstr.append(x)
            # print("-newstr :",newstr)
    return ''.join(newstr)

print(reverse_vowels2("Hello!") )# "Holle!" 
print(reverse_vowels2("Tomatoes")) # "Temotaos" 
print(reverse_vowels2("Reverse Vowels In A String") )# "RivArsI Vewols en e Streng"
print(reverse_vowels2("aeiou") )# "uoiea"
print(reverse_vowels2("why try, shy fly?") )# "why try, shy fly?"

print("-----------------lec------------------")
def reverse_vowels3(s):
    vowels = "aeiou"
    string = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
    return "".join(string)

