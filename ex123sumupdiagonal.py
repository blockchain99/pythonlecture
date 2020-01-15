'''
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
sum_up_diagonals(list2) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
sum_up_diagonals(list4) # 68
'''
## 4 by 4 -> index: ((0,0)+ (1,1) + (2,2) + (3,3)) +
## (0,3) (1,2) (2,1) (3,0)-> (a,b) a+b => N-1 a: 1,2,3..N

print("-------test3---N by N list make--with else clause--OK-index-")
def sum_up_diagonals3(alist): #N by N list
    # if ((row == column) or (row + column == len(alist) +1))
    return [[(row,column) if column %2 == 0 else None for column in range(0, len(alist[1]))] for row in range(0, len(alist[0]))]
test =[
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]    
print(sum_up_diagonals3(test))
print("-------test4---N by N list make--with else clause--OK--value")
def sum_up_diagonals4(alist): #N by N list
    
    ## one list consists of two diagonals-> not correct(duplated middle just once added !)
    # return  [[alist[row][column] if (column == row or row + column == len(alist) -1) else 0 for column in range(0, len(alist[1]))] for row in range(0, len(alist[0]))]
     
    
    ## make tuple of each diagonals
    # return ( [[alist[row][column] if column == row else 0 for column in range(0, len(alist[1]))] for row in range(0, len(alist[0]))]
    #  ,[[alist[row][column] if row + column == len(alist) -1 else 0 for column in range(0, len(alist[1]))] for row in range(0, len(alist[0]))] )
     
## TypeError 
    # diag1 = sum([[alist[row][column] if column == row else 0 for column in range(0, len(alist[1]))] for row in range(0, len(alist[0]))])
    # diag2 = sum([[alist[row][column] if row + column == len(alist) -1 else 0 for column in range(0, len(alist[1]))] for row in range(0, len(alist[0]))])
    # return diag1 + diag2

## 
    diag1 = sum(map(sum, [[alist[row][column] if column == row else 0 for column in range(0, len(alist[1]))] for row in range(0, len(alist[0]))]))
    diag2 = sum(map(sum, [[alist[row][column] if row + column == len(alist) -1 else 0 for column in range(0, len(alist[1]))] for row in range(0, len(alist[0]))]))
    return diag1 + diag2
    
test =[
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]    
print(sum_up_diagonals4(test)) #68 correct !!
list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
print(sum_up_diagonals4(list1)) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
print(sum_up_diagonals4(list2)) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

print(sum_up_diagonals4(list3)) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
print(sum_up_diagonals4(list4)) # 68

# print("-------test1---N by N list make- w/o else clause -> Invalid Syntax 'for' ----")
# def sum_up_diagonals(alist): #N by N list
#     # if ((row == column) or (row + column == len(alist) +1))
#     return [[(row,column) if column %2 == 0 for column in range(0, len(alist[1]))] for row in range(0, len(alist[0]))]
# test =[
#   [ 1, 2, 3, 4 ],
#   [ 5, 6, 7, 8 ],
#   [ 9, 10, 11, 12 ],
#   [ 13, 14, 15, 16 ]
# ]    


print("--------test------")
list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]

print(len(list4)) #4
print(len(list4[0])) #4
print(len(list4[1])) #4
print(list4[1][1]) #6

print("--multi dimension sum--sum(map(sum, alist)) -- sum(sum(x) for x in alist--")
print( sum(map(sum, list4)) ) #136 correct
print( sum(sum(x) for x in list4) )
print(1+6+11+16+4+7+10+13) #68

print("----------lec ver--------")
def sum_up_diagonals_lec(arr):
    total = 0
## 4 by 4 -> index: ((0,0)+ (1,1) + (2,2) + (3,3)) +
## (0,3) (1,2) (2,1) (3,0)-> (a,b) a+b => N-1 a: 1,2,3..N  -> b= N-1-a
    for i,val in enumerate(arr):
        total += arr[i][i]
        # total += arr[i][-1-i]
        total += arr[i][len(arr)-1-i]
    return total

print(sum_up_diagonals_lec(list4)) # 68
print(sum_up_diagonals_lec(list3)) # 11