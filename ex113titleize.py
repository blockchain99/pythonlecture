'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''

print("-------output: ['This ', 'Is ', 'Awesome '] -- need to be change!")

strlist = []
def titleize(astring):
    for word in astring.split(" "):
        strlist.append(word[0].upper()+word[1:]+" ")
    return strlist

print(titleize('this is awesome')) # "This Is Awesome"
print(titleize('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"

print("----------- 2nd approach --OK--------")

def titleize1(astring):
    string = ""
    for word in astring.split(" "):
        string += (word[0].upper()+word[1:]+" ")
    return string

print(titleize1('this is awesome')) # "This Is Awesome"
print(titleize1('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"

print("----------- 3nd approach -one line--with list--------")

def titleize2(astring):
    return "".join([word[0].upper()+word[1:]+" " for word in astring.split(" ")])

print(titleize2('this is awesome')) # "This Is Awesome"
print(titleize2('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"

print("####### lec ####just string ver###")
def titleize3(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))

print("---------- test ------------")
# def truncate(astring, num):
#     # return astring[:num-3]+"..." if num >= 3 else "Truncation must be at least 3 characters." #not perfect
#     return ((astring[:num-3]+"..." if len(astring) > num else astring) if num >= 3 else "Truncation must be at least 3 characters.") 
