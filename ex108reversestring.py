'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''

# add whatever parameters you deem necessary - good luck!
def reverse_string(input_str):
    # implement your function here
    print(input_str[::-1])

reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
print("--------same---------")
def reverse_string1(input_str):
    # implement your function here
    return input_str[::-1]

print(reverse_string1('awesome')) # 'emosewa'
print(reverse_string1('Colt')) # 'tloC'
print(reverse_string1('Elie')) # 'eilE'

print("--------lec--------")
def reverse_string2(str):
    s = ''
    for i, char in enumerate(str[::-1]):
        s += char
    return s

print(reverse_string2('awesome')) # 'emosewa'
print(reverse_string2('Colt')) # 'tloC'
print(reverse_string2('Elie')) # 'eilE'