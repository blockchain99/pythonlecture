import sqlite3
import requests
from bs4 import BeautifulSoup

# Request URl
response = requests.get("http://books.toscrape.com/catalogue/category/books/history_32/index.html")
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all('article')
# print(type(books))
# for book in books:
#     print(book)

all_books = []
str_to_num = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5}
for book in books:
    title = book.find("h3").find("a")["title"]
    print("*** Title ***",title)
    price = book.find(class_="price_color").get_text().replace("Â","").replace("£","")
    print("***price---",price)
   
    # print("***rating select---",book.select(".star-rating")[0]) #select return multiple instances, return list
    # print("***rating find---",book.find(class_="star-rating")) #same as above
    
    # using .get_attribute_list to show attribute 
    # print("***rating number---",book.find(class_="star-rating").get_attribute_list("class")) 
    # print("***just number---",book.find(class_="star-rating").get_attribute_list("class")[1]) 
    rating = str_to_num[book.find(class_="star-rating").get_attribute_list("class")[1]]
    print("***just interger number---",rating) 
    # print("***just number---",book.find(class_="star-rating").get_attribute_list("class")[-1]) #same as above
    print("----------------------------")
    
    # all_books.append([title, float(price), rating]) # list of lists
    all_books.append((title, float(price), rating)) # list of tuples
print("==================save to list & db=========================")
print(all_books)

conn = sqlite3.connect("test366scrapdb.db")
c = conn.cursor()
c.execute("CREATE TABLE books (title TEXT, price REAL, rating INTEGER);")

sql_insert = "INSERT INTO books VALUES (?,?,?)"
c.executemany(sql_insert, [element for element in all_books])

sql_list = [
    "SELECT * FROM books WHERE price > 30",
    "SELECT title FROM books WHERE price > 30 ORDER BY price",
    "SELECT * FROM books WHERE rating == 4 "
]
number = 1
for sql in sql_list:
    print(f"------SELECT RESULT--- {number} Query --------")
    c.execute(sql) #Cursor object
    print("---",c.fetchone())
    number += 1
print("========================================")
c.execute("SELECT * FROM books")
print(c.fetchall())
conn.commit()
conn.close()