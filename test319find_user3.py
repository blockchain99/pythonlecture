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

print("-----def find_user()------------------")
from csv import reader
def find_user(first, last):
    with open("users1.csv") as file:
        csv_reader = reader(file)
        for (index, row) in enumerate(csv_reader):
            fisrt_name_found = first == row[0]
            last_name_found = last == row[1]
            if fisrt_name_found and last_name_found:
                return index 
            # return "Not found " #Not as intended
        return "Not found" #after all loop ended, if not found -> then return msg.
        # w/o above line, just return None
print(find_user("Colt","Steele"))
print(find_user("Grace","Hopper"))        
print(find_user("Alan","Turing"))
print(find_user("James","Turing"))

print("==============")
	
