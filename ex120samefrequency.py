'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''
def same_frequency(num1,num2): #same frequecy of digit -> True
    str_num1 = str(num1)
    str_num2 = str(num2)
    count_dict1 = {digit: str_num1.count(digit) for digit in str_num1}
    print("** count_dict1: ", count_dict1)
    count_dict2 = {digit: str_num2.count(digit) for digit in str_num2}
    print("** count_dict2: ", count_dict2)
    return  all(count_dict1.get(x) == count_dict2.get(x) for x in count_dict1)
print(same_frequency(551122,221515)) # True
print(same_frequency(321142,3212215)) # False
print(same_frequency(1212, 2211) )# True

print("---------lec-----")
def same_frequency1(num1,num2):
    d1 = {letter:str(num1).count(letter) for letter in str(num1)}
    d2 = {letter:str(num2).count(letter) for letter in str(num2)}
  
    for key,val in d1.items():
        if not key in d2.keys():
            return False
        elif d2[key] != d1[key]:
            return False
    return True
