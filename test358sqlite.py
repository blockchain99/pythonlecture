#https://likegeeks.com/python-sqlite3-tutorial/
# https://www.sqlite.org/lang.html (sqlite keyword chart diaagram)

# create a connection object to connect us to the database
import sqlite3
con = sqlite3.connect('mydatabase.db')

#cursor object : method of the connection object. 
con = sqlite3.connect("mydatabase.db")
cursorObj = con.corsor()

## create db ##

import sqlite3
 
from sqlite3 import Error
 
def sql_connection():
 
    try:
 
        con = sqlite3.connect(':memory:')
 
        print("Connection is established: Database is created in memory")
 
    except Error:
 
        print(Error)
 
    finally:
 
        con.close()
 
sql_connection()

#Create Table
import sqlite3
 
from sqlite3 import Error
 
def sql_connection():
 
    try:
 
        con = sqlite3.connect('mydatabase.db')
 
        return con
 
    except Error:
 
        print(Error)
 
def sql_table(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
 
    con.commit()
 
con = sql_connection()
 
sql_table(con)

#insert table 1
cursorObj.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")
 
con.commit()

#insert table 2 - 

import sqlite3
 
con = sqlite3.connect('mydatabase.db')
 
def sql_insert(con, entities):
 
    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    
    con.commit()
 
entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
 
sql_insert(con, entities)

#update table
import sqlite3
 
con = sqlite3.connect('mydatabase.db')
 
def sql_update(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
 
    con.commit()
 
sql_update(con)

#select 
cursorObj.execute('SELECT * FROM employees ')
cursorObj.execute('SELECT id, name FROM employees')

#Fetch all data 1
import sqlite3
 
con = sqlite3.connect('mydatabase.db')
 
def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT * FROM employees')
 
    rows = cursorObj.fetchall()
 
    for row in rows:
 
        print(row)
 
sql_fetch(con)

#Fetch all data 2
[print(row) for row in cursorObj.fetchall()]

#Fetch : fetch id and names of those who have a salary greater than 800
import sqlite3
 
con = sqlite3.connect('mydatabase.db')
 
def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')
 
    rows = cursorObj.fetchall()
 
    for row in rows:
 
        print(row)
 
sql_fetch(con)

#row count:  return the number of rows that are affected 
# or selected by the latest executed SQL query.
print(cursorObj.execute('SELECT * FROM employees').rowcount)


#row count 2 : 
# When we use rowcount with the SELECT statement, 
# -1 will be returned as how many rows are selected 
# is unknown until they are all fetched
#-> T'4 herefore, to get the row count, you need to fetch 
# all the data, and then get the length of the result
rows = cursorObj.fetchall()
 
print len (rows)

# list table
import sqlite3
 
con = sqlite3.connect('mydatabase.db')
 
def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
 
    print(cursorObj.fetchall())
 
sql_fetch(con)

#check if table exists or not
import sqlite3
 
con = sqlite3.connect('mydatabase.db')
 
def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('create table if not exists projects(id integer, name text)')
 
    con.commit()
 
sql_fetch(con)

#if table exits delete table
cursorObj.execute('drop table if exists projects')

#check if the table we want to access exists or not
cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "employees"')
 
print(cursorObj.fetchall())

# drop/delete a table using the DROP statement
import sqlite3
 
con = sqlite3.connect('mydatabase.db')
 
def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('DROP table if exists employees')
 
    con.commit()
 
sql_fetch(con)