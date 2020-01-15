nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(nested_list[0][1]) # 2

print(nested_list[1][-1]) # 6
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("++=====very important====++")
print("-----option1----")
for l in nested_list:
    for val in l:
        print(val)
print("-----option2----")
[[print(val) for val in l] for l in nested_list]
print("=============flat list from nested list===========****")
b_nested = [[2, 4, 6, 8], [1, 3, 5, 7, 9]]
print([element for alist in b_nested for element in alist])

print("---- [n for n in range(1,4)] for val in range(1,4)---")
board = [[num for num in range(1,4)] for val in range(1,4)]

print(board) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

print([["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)])
# [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]

print("==== np.array only!!====")
print("-----for a_element, b_element cond in zip(A,B,condition)---")
import numpy as np
# numpy where
A = np.array([1,2,3,4])
B = np.array([100,200,300,400])
condition = np.array([True,True, False, False])
# slow way
zip(A,B,condition)
#[(1, 100, True), (2, 200, True), (3, 300, False), (4, 400, False)]
answer1 = [a_elem if cond else b_elem for a_elem, b_elem, cond in zip(A,B,condition)]
print(answer1)
[1, 2, 300, 400]

## fast way. np.where(condition,A,B)
print(np.where(condition, A,B))
print("---------nested list------------")
# nested_list = [[value for value in range(0, 10)] for l in range(0,10)]
nested_list= [[num for num in range(0,10)] for val in range(0,10)]
print(nested_list)
for l in nested_list:
    for v in l:
        print(v)
print("---------intersection of two lists----")
print([val2 for val2 in [1,2,3,4] if val2 in [3,4,5,6]])

print("======= list comprehension: even number from list=====")
print([v for v in range(1, 10) if v % 2 ==0 ])

print("---option2 --")
answer = []
for x in [1,2,3,4]:
    if x in [3,4,5,6]:
        answer.append(x)
print(f"answer: {answer}")        
answer2 = []
print("]]]]]]]")
print([ name[::-1].lower() for name in ["Elie", "Tim", "Matt"]])
for name in ["Elie", "Tim", "Matt"]:
    answer2.append(name[::-1].lower())
print("==============")
answer = [char for char in "amazing" if char not in ["a", "e","i","o","u"]]
print(answer)
