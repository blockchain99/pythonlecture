
########### index of ordereddict ######
# from collections import OrderedDict

# x = OrderedDict('test1'='a', 'test2'='b')
# print(list(x.keys().index('test1'))
#########################################

print("------------reader-------------------")
# Reading/Parsing CSV Using a DictReader:
from csv import reader

def find_user(first_name, last_name):

    with open("users1.csv") as file:
        csv_reader = reader(file)
        next(csv_reader) #skip header
        index_user = 0
        for f in csv_reader:
            if f[0] == first_name and f[1] == last_name:
                print({f"{f[0]} is from {f[1]}"})
                print(f"index : {index_user}")
                print("----end of found---")
            else:
                print(f" No user found for index : {index_user}")
            index_user += 1
    
find_user("Colt","Steele")        
# find_user("Grace","Hopper")        
# find_user("Alan","Turing")        
print("-----------+++++++++++")
######## lec ver #########
# import csv
 
# def find_user(first_name, last_name):
#     with open("users.csv") as csvfile:
#         csv_reader = csv.reader(csvfile)
#         for (index, row) in enumerate(csv_reader):
#             first_name_match = first_name == row[0]
#             last_name_match = last_name == row[1]
#             if first_name_match and last_name_match:
#                 return index
#         return "{} {} not found.".format(first_name, last_name)