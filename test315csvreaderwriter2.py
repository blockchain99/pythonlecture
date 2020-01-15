#read csv  and covert to upper case in writerow state & save as new name

############ 
#reader() : Return a reader object which will iterate over lines
############
from csv import reader, writer
with open("test305.csv") as file:
    csv_reader = reader(file) #alrady list-return lines of list
    ## nested list for element <- rows <- whole text
    ##read whole csv -> for each rows -> for each element -> upper case
    # uppers =  [[x.upper() for x in row]for row in csv_reader]
    # for row in uppers:
    #     print(row)

####### since reader return linse of list, indented writer -> just one loop 
## of writer needed !!!--> without indented writer module -> open file closed
## -> Error occurres!!
    with open('test305upper2.csv', "w") as file: #seperate open to write as new name.
        csv_writer = writer(file)
        for element in csv_reader:
            csv_writer.writerow([x.upper() for x in element])
