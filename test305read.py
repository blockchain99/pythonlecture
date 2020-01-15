with open("test305haiku.txt", "r") as file:
    result = file.read()
    print(result)

print("==== reader for csv======")
from csv import reader
with open("test305.csv") as file:
    wholecsv = reader(file)
    for row in wholecsv: #each row in a list
        print(row)
print("==== DictReader for csv======")
print("====OrderedDictionary: Remember the Order Keys are Added to a Dictionary=")
from csv import DictReader
with open("test305.csv") as file:
    dictwholecsv = DictReader(file)
    for row in dictwholecsv: #row of OrderedDict
        print(row)


