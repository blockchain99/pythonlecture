import sqlite3
conn = sqlite3.connect("test361friends.db")
# create cursor object
c = conn.cursor()
# c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")


# Iterate over cursor
# for result in c:  #Once these 2 lines excuted, below c.fetchall() -> no return. 
# 	print(result)
print("---------------------------------")
# Fetch One Result
# print(c.fetchone())

# Fetch all results as list
print(c.fetchall())


# commit changes
conn.commit()
conn.close()