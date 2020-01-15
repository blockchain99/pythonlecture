import sqlite3
conn = sqlite3.connect("users.db")

# query = "CREATE TABLE users (username TEXT, password TEXT)"
u = input("please enter your username...")
p = input("please enter your password...")
c = conn.cursor()

c.execute("CREATE TABLE users (name TEXT, username TEXT, password TEXT)")
people = [
	("Roald","amu", "pass1"),
	("Rosa", "park", "thispass2"),
	("Henry", "hudson","pass3*"),
	("Neil","trog75", "password3"),
	("Daniel", "boogine", "mypass3")
	]
query1 = f"INSERT INTO users VALUES (?,?,?)"
# for element in people:
# 	c.execute(query1, element)
c.executemany(query1, people)
# THE BAD WAY!
# query = f"SELECT * FROM users WHERE username='{u}' AND password = '{p}'"
##'SELECT * FROM users WHERE username='Colt' AND password = '' OR 1=1' #WRONG
## username : .. , password : ... OR 1=1--  -> makes pwd correct!

# THE MUCH SAFER WAY
query = f"SELECT * FROM users WHERE username=? AND password =?"
c.execute(query,(u,p))

result = c.fetchone()
# result = c.fetchall()
if(result):
	print("WELCOME BACK")
else:
	print("FAILED LOGIN")

conn.commit()
conn.close()
