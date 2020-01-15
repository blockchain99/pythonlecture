from csv import reader, writer

with open("users3.csv") as file:
    csv_reader = reader(file)  #Once printed, this var can't be excuted to show result!!
    print(type(csv_reader))
   
    print("------------csv_reader for loop -: same as blow-----")
    for a in csv_reader:
        print(a)


    # # print("------------list(csv_reader) for loop ------")
    # # rows = list(csv_reader)
    # # print(type(rows))
    # # print(rows)

    # for r in list(csv_reader):
    #     print(r)

