'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''
from csv import reader, writer
def delete_users(first, last):
    with open("users5.csv") as file:
        csv_reader = reader(file)
        rows = list(csv_reader)
    count = 0
    with open("users5.csv", "w") as file:
        csv_writer = writer(file)
        for row in rows:
            if row[0] == first and row[1] == last:
                # csv_writer.writerow('')#nothing do -> no writing for this row -> remove
                count += 1
            else:
                csv_writer.writerow(row)
    print("Users deleted: {}".format(count))





delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.