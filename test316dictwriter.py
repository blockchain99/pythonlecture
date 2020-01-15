# from csv import writer, DictWriter
# print("---------- Version using writer--------")
# with open("cats3.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Name", "Age"])
#     csv_writer.writerow(["Blue", 3])
#     csv_writer.writerow(["Kitty", 1])

# print("## ----------Version using DictWriter-------")
# with open("cats33.csv", "w") as file:
# 	headers = ["Name", "Breed", "Age"]
# 	csv_writer = DictWriter(file, fieldnames=headers)
# 	csv_writer.writeheader()
# 	csv_writer.writerow({
# 		"Name": "Garfield",
# 		"Breed": "Orange Tabby",
# 		"Age": 10
# 	})


print("####### DictReader, convert cm to in and DictWriter as new dict #####")
from csv import DictReader, DictWriter

def cm_to_in(cm):
    return int(float(cm) * 0.393701)

with open("test305.csv") as file:
    csv_reader = DictReader(file) 
    # print(csv_reader) #DictReader obj
    print("--------fighters = list(csv_reader)------")
    # csv_reader = list(csv_reader)
    # print(csv_reader)  # above tow lines cause no writerow() 
    fighters = list(csv_reader)

with open("test305_inches.csv", "w") as file:
    headers = ("Name", "Country", "Height")
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for f in fighters:
        # csv_writer.writerow(f) #maybe error

        csv_writer.writerow({
            "Name" : f["Name"],
            "Country" : f["Country"],
            "Height" : cm_to_in(f["Height (in cm)"])
        }) 
