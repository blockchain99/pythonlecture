from csv import writer, DictWriter
print("## ----------- writer------------")
print("==creates an object that lets you take lists of data \
and write rows into a CSV")

with open("cats.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Blue", 3])
    csv_writer.writerow(["Kitty", 1])

# with open("cats.csv", "r") as file: #BAD!!
#     catsfile = file.read()
#     print(catsfile)
print(" -- reader() from ** writed cats.csv-- ")
from csv import reader
with open("cats.csv") as file:
	csv_reader = reader(file)

	# print(list(csv_reader)) #option 1

	for row in csv_reader:  #option 2
		print(row)

print("-----------DicWriter--------------------")
# Version using DictWriter
with open("cats2.csv", "w") as file:
	headers = ["Name", "Breed", "Age"]
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	csv_writer.writerow({
		"Name": "Garfield",
		"Breed": "Orange Tabby",
		"Age": 10
	})

with open("cats2.csv", "r") as file:
	lines = file.readlines()
	print(lines)
print("-------------------")
with open("cats2.csv", "r") as file:
	result = file.read()
	print(result)