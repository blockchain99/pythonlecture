'''
sum_pairs([4,2,10,5,1], 6) # [4,2] 4+2 -> 6 
sum_pairs([11,20,4,2,1,5], 100) # []
'''
#accept list and number as input, first pair of numbers 
# that sum to the number passed to the function.
from itertools import permutations, combinations
def sum_pairs1(alist):
    for e in combinations(alist, 2):
        print(e)
        # return e  #just print(4,2) only -> wrong!

# print(sum_pairs([4,2,10,5,1]))
sum_pairs1([4,2,10,5,1])
print("--------------------------")
for x in combinations([4,2,10,5,1], 2):
    print(x)

print("=============solution with combination================")
def sum_pairs2(alist, num): 
    for e in combinations(alist, 2): 
        if sum(e) == num:
            return list(e)
    return []        
        
print(sum_pairs2([4,2,10,5,1], 6)) # [4,2The remove() method only removes the given element from the list. It doesn't return any value.] 4+2 -> 6 
print(sum_pairs2([11,20,4,2,1,5], 100)) #The remove() method only removes the given element from the list. It doesn't return any value.[] 
print("------------------two-for loop ---------")
def pairs(alist, num):
        for i in range(0, len(alist)-1):
            for j in range(i+1, len(alist)):    
                if (alist[i] + alist[j]) == num:
                        return [alist[i], alist[j]]
        return []

print(pairs([4,2,10,5,1], 6)) # [4,2] 4+2 -> 6 
print(pairs([11,20,4,2,1,5], 100)) 

print("------lec ver: (list,num) return : (num - element in list) == it's next element----

print("------test------")
animal = ['cat', 'dog', 'rabbit', 'guinea pig', 'camel']
#The remove() method only removes the given element from the list. 
# It doesn't return any value.
xx=  animal.remove('dog')
print(xx) #None
print(animal)
print(animal.pop(-2)) #return this one. 
print(animal)
