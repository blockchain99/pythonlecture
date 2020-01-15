'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''
from csv import writer
def add_user(first_name, last_name):
    with open("test317users.csv", "a") as file:
	    csv_writer = writer(file)
	    csv_writer.writerow({
		   first_name, last_name
	    })   
add_user("Dwayne", "Johnson")


##### This is  wrong version #######
######## with open(x.csv, "w") as file ######
## remove existing csv and write new
## DictWrite(x.csv, "a") -> header added to existing.

# from csv import DictReader, DictWriter
# with open("test317users.csv") as file:
#     csv_reader = DictReader(file) 
#     fighters = list(csv_reader)

# with open("test317users.csv", "a") as file:
#     headers = ("First Name", "Last Name")
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "First Name" : "Dwayne",
#         "Last Name" : "Johnson"
#     })