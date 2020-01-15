# Create a list called instructors
instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
 
instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")
print(instructors)

instructors2 = []
instructors2.extend(["Colt", "Blue", "Lisa"])
print(instructors2)

## make list with elements
instructors3 = ["Colt", "Blue", "Lisa"]
print(instructors3)

instructors3.clear()
print(f"after list_name.clear() : {instructors3}")


#### pop : remove the item at the given position in the list, and return it
### if no index is specified, removes & returns last item in the list. 
# instructors2.pop("Lisa")
# print(f"after list_name.pop() : {instructors2}")#TypeError: 'str' object cannot be interpreted as an integer

instructors2.pop()
print(instructors2)
instructors2.append("Lala")

print("--- instructor2: ",instructors2)
removed_positon1_item = instructors2.pop(1) #remove item at position 1, which is "Blue"
print("* removed item at positon 1:",removed_positon1_item)
print(instructors2)
instructors2.insert(1, "Tom") #list.insert( index. obj)
print(instructors2)
print("-------------------")

##remove : remove the first item from the list whose value is x. 
#throw ValueError if the item is not found. 
first_list  = [1 ,2, 3, 4, 4, 4]
first_list.remove(4)
print(first_list)

##.index(x) : return element x's first positoin, 
##.index(x, start_positon) x's frist position from start_positon
## .index(x, start_postion, end_positoin) x's frist position between start, end

##.count : return the number of times x appears in the list.
print(first_list.count(4))
