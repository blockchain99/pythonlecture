'''
nth(['a', 'b', 'c', 'd'], 1)  # 'b' 
nth(['a', 'b', 'c', 'd'], -2) #  'c'
nth(['a', 'b', 'c', 'd'], 0)  # 'a'
nth(['a', 'b', 'c', 'd'], -4) #  'a'
nth(['a', 'b', 'c', 'd'], -1) #  'd'
nth(['a', 'b', 'c', 'd'], 3)  # 'd'
'''

def nth(alist, num): #return element of given number index
    return alist[num]

print(nth(['a', 'b', 'c', 'd'], 1))  # 'b' 
print(nth(['a', 'b', 'c', 'd'], -2)) #  'c'
print(nth(['a', 'b', 'c', 'd'], 0) ) # 'a'
print(nth(['a', 'b', 'c', 'd'], -4) )#  'a'
print(nth(['a', 'b', 'c', 'd'], -1) )#  'd'
print(nth(['a', 'b', 'c', 'd'], 3)  )# 'd'

print("-------lec-------")
def nth1(arr, idx):
    if idx >= 0:
        return arr[idx]
    return arr[idx + len(arr)]