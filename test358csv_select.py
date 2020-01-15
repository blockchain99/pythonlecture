import csv, sqlite3

con = sqlite3.connect("test358profile_csv.db")
cur = con.cursor()
query_list = [
    "SELECT * FROM profile WHERE Name IS 'Ken';",
    "SELECT * FROM profile WHERE Country IS 'China';",
    "SELECT Name FROM profile WHERE Country IS 'Japan';",
    "SELECT * FROM profile WHERE Country IS NOT 'USA';",
    "SELECT * FROM profile WHERE Country IS NOT 'USA' AND Country IS NOT 'Brazil';",
    "SELECT * FROM profile WHERE Height > 68;",
]
for query_element in query_list:
    print(cur.execute(query_element).fetchall())

print("--------------------------------------")
cur.execute("SELECT * FROM profile;")
for result in cur:
    print(result)

print("--------fetchall()-> in single list--------") 
cur.execute("SELECT * FROM profile;")   
print(cur.fetchall()) 
# print(cur.fetchone()) 
print("--------fetchone()-> show one --------") 
# cur.execute("SELECT * FROM profile WHERE Height > 68 ORDER BY Height")   
cur.execute("SELECT * FROM profile WHERE Height > 68")   
# cur.execute("SELECT * FROM profile WHERE Height > 68;")   
print(cur.fetchall()) 
con.commit()
con.close()