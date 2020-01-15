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

# for e in data_list:
#     c.execute(query, e)

c.executemany(query, [element for element in data_list])

## insert opt 1
insert_query = '''INSERT INTO dogs 
                    VALUES ('Jonadon', 'Johnson', 9)'''
c.execute(insert_query)


query_list =[
    "SELECT * FROM dogs WHERE name IS 'Delma';",
    "SELECT * FROM dogs WHERE breed IS 'shepard';",
    "SELECT name FROM dogs WHERE breed IS 'shepard';",
    "SELECT * FROM dogs WHERE breed IS NOT 'border coli';",
    "SELECT * FROM dogs WHERE breed IS NOT 'husky' AND breed IS NOT 'border coli';",
    "SELECT * FROM dogs WHERE age > 3;",
]
# for query_element in query_list:
#     print(c.execute(query_element)) #cursor obj
for query_element in query_list:
    print(c.execute(query_element).fetchall())
conn.commit()
conn.close()
