## slicing list: list[start:end:step] #end is not included.
test_list = list(range(1,10))
print(test_list)
sliced_list = test_list[2:5]
print(sliced_list)

sliced_list2 = test_list[1:6:2]
print(sliced_list2)
print("----------------")
first_list = list(range(1, 9)) # 1 ~ 8
print(first_list)
print(first_list[1:])
print(first_list[:3])
print("==========")
print(first_list[2:6]) #position 6 not included
print(first_list[2:6:2])
print(first_list[:])
print("+++++end is -1, which is last element- excluded +++++++++++")
print(first_list[:-1]) # -1, last element excluded
print(first_list[1:-1])
print(f"first_list[::2] is  {first_list[::2]}")

first_list_copy = first_list[:]
print(bool(first_list == first_list_copy))
print(bool(first_list is first_list_copy))
print("==--++======")

list_two = [1,2,3,4,5,6]
print(list_two[::2])
print(list_two[::-1])

