#return how many updated,

from csv import reader, writer

with open("users22.csv") as file:
    csv_reader = reader(file)  #Once printed, this var can't be excuted to show result!!
    # print(type(csv_reader))
    rows = list(csv_reader)
    # print(rows)

with open('users22.csv', "w") as file:
    csv_writer = writer(file)
    # for row in rows:
    for row in csv_reader: #ValueError: I/O operation on closed file.
        # print(row)  #test
        first_matched = row[0] == "Colt" 
        last_matched =  row[1] == "Steele"
        if first_matched and last_matched:
            row[0] = "Boba"
            row[1] = "Fett"
            csv_writer.writerow(row)
            print( 2 )
        elif first_matched != last_matched: #exclusive or if var is boolean.
            csv_writer.writerow(row)
            print( 1)
        else:
            csv_writer.writerow(row)
            print(0)



############## wrong output: "w" -> remove all write each row.####
# from csv import reader, writer
# def update_users(old_first, old_last, new_first, new_last):
#     with open("users2.csv") as file:
#         csv_reader = reader(file) 
#       
#     with open('users2.csv', "w") as file:
#         csv_writer = writer(file)
#         for row in csv_reader:
#             print(row)
#             first_matched = old_first == row[0]
#             last_matched = old_last == row[1]
#             if first_matched and last_matched:
#                 row[0] = new_first
#                 row[1] = new_last
#                 csv_writer.writerow(row)
#                 return 2
#             elif first_matched != last_matched: #exclusive or if var is boolean.
#                 return 1 # w/o writerow -> it change to blank row. 
#             else:
#                 return 0 # w/o writerow -> it change to blank row



# print(update_users("Grace", "Hopper", "Hello", "World")) # Users updated: 1.
# print(update_users("Colt", "Steele", "Boba", "Fett")) # Users updated: 2.
# print(update_users("Not", "Here", "Still not", "Here")) # Users updated: 0.
