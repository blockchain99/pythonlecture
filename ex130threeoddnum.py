'''
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''

def three_odd_numbers(alist):#3 any of consecutive num sum to odd num: T
    return any([True if sum(alist[i:i+3])%2 == 1 else False for i in range(0, len(alist)-2)])

print(three_odd_numbers([1,2,3,4,5])) # True
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
print(three_odd_numbers([5,2,1])) # False
print(three_odd_numbers([1,2,3,3,2])) # False

print("##################test list################")
test1 = [1,2,3,4,5]
print(test1[1:3]) #index1(val 2), index2(val 3) only -> index 3 not incl
print(test1[0:3]) #index0, 1, 2 only -> index 3 not incl
print("======loop test--")
for i in range(0, 3): # index 0,1,2 (3 elements) last 3 index not incl.
    print(test1[i])
    print(test1[i:i+3]) #3 elemts, last i+3 not incl. 
    print("-----")
print("======loop test-2 with len(alist): range(0, 5-2)-> (0,3)-> 0,1,2: 3 elements")
for i in range(0, len(test1)-2): # 0,1,2,3 (4 elements) last 4 index not incl.
    print(test1[i])
    print(test1[i:i+3]) #3 elemts, last i+4 not incl. 
    print("-----")

print("----------lec-------------")
def three_odd_numbers1(arr):
    i = 0
    while(i < (len(arr) -2)):
        total = 0
        j = i
        while(j <= i+2):
            total += arr[j]
            j+=1
            
        if (j-i) % 3 == 0 and total % 2 != 0:
            return True
            
        i+= 1
    return False