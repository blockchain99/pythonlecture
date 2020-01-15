#rad csv then covert to upper case in read state and save as new name
from csv import reader, writer
with open("test305.csv") as file:
    csv_reader = reader(file) #reader class obj -> to show, list convert or for loop
    ## nested list for element <- rows <- whole text
    ##read whole csv -> for each rows -> for each element -> upper case
    
    print("-------- reader obj : csv_reader-------")
    # print(csv_reader)
    print("#####just test purpose : list(csv_reader)####") 

    print("### end of test###")
    uppers =  [[x.upper() for x in row]for row in csv_reader] # reader obj -> list
    for row in uppers: #If above csv_reader printed this for loop : no show!
    # print(list(csv_reader))
        print(row)

with open('test305upper.csv', "w") as file: #seperate open to write as new name.
    csv_writer = writer(file)
    for upper in uppers:
        csv_writer.writerow(upper)
