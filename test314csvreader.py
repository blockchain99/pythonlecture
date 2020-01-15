# THIS DOES READ THE FILE BUT IT DOESN'T PARSE IT!
# BAD!!!!!!
# with open("fighters.csv") as file:
#     data = file.read()
print("--------------reader-->as list-----------------")
# Using reader
from csv import reader
# with open("fighters.csv") as file:
with open("test305.csv") as file:
    csv_reader = reader(file)
    next(csv_reader) #To skip the headers
    for fighter in csv_reader:
    	# Each row is a list
    	# Use index to access data
    	print(f"{fighter[0]} is from {fighter[1]}") 
print("---------------cast to list ----------------")
# Example where data is cast into a list
from csv import reader
# with open("fighters.csv") as file:
with open("test305.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)
    print(data)

print("-------------DictReader-------------------")
# Reading/Parsing CSV Using a DictReader:
from csv import DictReader
# with open("fighters.csv") as file:
with open("test305.csv") as file:
    csv_reader = DictReader(file)

    # print("---+++---+++")
    # print(list(csv_reader)) # make itrable to iterator(list)
    # print("-------===-------===---")

    for row in csv_reader:
    #     ## Each row is an OrderedDict!
        print(row['Name']) #Use keys to access data
    #     print(row) 
        # print(list(row)) #only list of key -> header