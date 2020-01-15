'''
min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
'''

def min_max_key_in_dictionary(adict):
    sum_keys = sum(adict.keys()) 
    min_keys = min(adict.keys())
    print(sum_keys)
    print("*min",min_keys)
    print("*max",max(adict.keys()))
# print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'})) # [1,10]
# print(min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"})) # [1,4]

min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]


print("--------------test---------------------")
testdict = {2:'a', 7:'b', 1:'c',10:'d',4:'e'}
print(testdict.values())
print("-----generator to list-----")
key_int = [key for key in testdict.keys() ]#generator obj
print(key_int)
sumresult = sum(testdict.keys())
print(sumresult)

def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line

print("---test2 --nested list sum -> [ sum_of_list, sum_of_list]---")
a = [[1,2,3], [2,1,4], [4,3,6]]
## shoud be result = [6,7,13]

print (map(sum, a)) #map object
print( [sum(b) for b in a] ) 

print("------lec ver--------")
def min_max_key_in_dictionary_lec(d):
    keys = d.keys()
    return [min(keys), max(keys)]