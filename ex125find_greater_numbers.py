'''
find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''
#[6,1,2,7] -> 6 : 0, 
# 1: 0
# 2: 1(1)
# 7: 3(6,1,2) , so total is 4: 
from itertools import permutations, combinations
def find_greater_numbers_p(alist):
    tuple_permutations = list(permutations(alist,2))
    return(tuple_permutations)
def find_greater_numbers_c(alist):
    tuple_combinations = list(combinations(alist,2))
    return(tuple_combinations)
def find_greater_numbers_combi(alist): #list of tuples # correct result!!
    tuple_combinations = list(combinations(alist,2))
    result = sum([1 if a < b else 0 for (a,b) in tuple_combinations])
    return result

print("-------number greater than previous element---OK!!-----")
def find_greater_numbers(alist):
    return sum(map(sum,list([1 if alist[i] > x else 0 for x in alist[:i]]for i in range(1, len(alist)))) )

print(find_greater_numbers([1,2,3])) # 3 
print(find_greater_numbers([6,1,2,7])) # 4
print(find_greater_numbers([5,4,3,2,1])) # 0
print(find_greater_numbers([])) # 0

print("-----premutations, combinations ===")
print(find_greater_numbers_p([1,2,3])) # 3 
print(find_greater_numbers_c([1,2,3])) # 3 
print(find_greater_numbers_p([5,4,3,2,1])) 
print("-------number greater than previous element-combination OK!----")
print(find_greater_numbers_combi([1,2,3])) # 3 
print(find_greater_numbers_combi([6,1,2,7])) # 4
print(find_greater_numbers_combi([5,4,3,2,1])) # 0
print(find_greater_numbers_combi([])) # 0

print("-------**--------")
testl = [6,1,2,7]
testla = [5,4,3,2,1]
print([testl[i] for i in range(1, len(testl))]) #[1,2,7]
print([testl[i-1] for i in range(1, len(testl))]) #
print([testl[i-1] for i in range(1, len(testl))]) #
print(list([1 if testl[i] > x else 0 for x in testl[:i]]for i in range(1, len(testl))))

print("##Nested loop:compare value of index i with all values from 0 index to i-1 index")
print("-----test------nested list sum-> sum(map(sum, alist..)-correct---------------------------------------------")
print(sum(map(sum,list([1 if testl[i] > x else 0 for x in testl[:i]]for i in range(1, len(testl)))) )) #4
print(sum(map(sum,list([1 if testla[i] > x else 0 for x in testla[:i]]for i in range(1, len(testla)))) )) #0

print("----------lec-----------")
def find_greater_numbers_lec(arr):
    count = 0
    i = 0
    j = 1
    while i < len(arr):
        while j < len(arr):
            if arr[j] > arr[i]:
                count += 1
            j+=1
        j = i+1
        i+=1
    return count