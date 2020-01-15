# Enumerate() method adds a counter 
# to an iterable and returns it 
# in a form of enumerate object
l1 = ["eat","sleep","repeat"] 
s1 = "geek"

# creating enumerate objects 
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 

print(f"Return type: {type(obj1)} ")
for e in obj1:
	print("****",e)
print( list(enumerate(l1)) )

# changing start index to 2 from 0 
print( list(enumerate(s1,2)) )

print("-----------------------")
from csv import reader
# def find_user(first, last):
# Colt,Steele -> 1st row: row[0] is 'Colt', row[1] is 'Steel'

with open("users1.csv") as file:
 #reader obj w/ multi line of lists
	csv_read = reader(file)
	# print("--- Once this line excuted, below for loop, no show result!---")
	# print(list(enumerate(csv_read)))  #
	# print("---- end of test----")

	for (index, row) in enumerate(csv_read):
		print(index, row[0], row[1])
print("==============")
	# for (index, row) in enumerate(csv_read):
	# 	if row[0] == "Colt" and row[1] == "Steel":
	# 		print(index)
	# 	print("Not found!")

