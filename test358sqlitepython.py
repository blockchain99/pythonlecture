import sqlite3
conn = sqlite3.connect("test358dog_db.db")
c = conn.cursor()
c.execute("CREATE TABLE dogs (name TEXT, breed TEXT, age INTEGER);")

# data = (("Delma", "husky", 5), ("baprk","shepard", 3),("Lubi","border coli",9)) #error binding, unsupported type
# data = ("Delma", "husky", 5), ("baprk","shepard", 3),("Lubi","border coli",9)#error binding, unsupported type
data_list = [("Delma", "husky", 5), ("baprk","shepard", 3),("Lubi","border coli",9)]
query = "INSERT INTO dogs VALUES (?,?,?)"
# query = "INSERT INTO dogs (name, breed, age) VALUES (?,?,?)"

# for i in range (0, len(data_list)):
#     c.execute(query, data_list[i])

    # print("Inserting now")

# for e in data_list:
#     c.execute(query, e)

c.executemany(query, [element for element in data_list])

print(c.execute("SELECT * FROM dogs"))
print("----------------------")
for result in c:
    print(result)
print("----------------------")
# print(c.fetchall()) #same as above. 
conn.commit()
conn.close()
