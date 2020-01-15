import csv, sqlite3

# con = sqlite3.connect(":memory:")
con = sqlite3.connect("test358profile_csv.db")
cur = con.cursor()
cur.execute("CREATE TABLE profile (Name TEXT,Country TEXT,Height INTEGER);") # use your column names here

with open('test358.csv','r') as file: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    csv_reader = csv.DictReader(file) # comma is default delimiter
    to_db = [(row['Name'], row['Country'], row['Height']) for row in csv_reader]

cur.executemany("INSERT INTO profile (Name, Country, Height) VALUES (?, ?, ?);", to_db)
con.commit()
con.close()