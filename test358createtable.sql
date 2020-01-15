CREATE TABLE dogs (
    name TEXT,
    breed TEXT,
    age INTEGER
);
############ option1 #######command is capital !!###
$ sqlite3 test.sl3 
sqlite> create table dogs (name TEXT, breed TEXT, age INTEGER);
sqlite> insert into dogs values('Lews', 'Border Coli', 4);
sqlite> insert into dogs (name, breed, age) values('Lews1', 'Border Coli1', 10);
sqlite> insert into dogs values('Delma', 'Shepard', 9);
sqlite> select * from dogs;
.quit  #crtl + d

## no .save -> Now load the databse again.
$ sqlite3 test.sl3
sqlite> select * from dogs;   # shows result.

############## option2 #########
##sqlite> .save cats_db.db after creeate table.. for saving.
##sqlite> .backup main cats_db.db 
###################################
#$ sqlite3
sqllite> create table cats (name TEXT, breed TEXT, age INTEGER);
sqlite> insert into cats values('King', 'Persian', 2);
sqlite> insert into cats values('Kong', 'Boland', 5);
sqlite> .backup main cats_db.db
sqlite> .quit #ctrl _ db
###
$ sqlite3 cats_db.db
sqlite> .schema
sqlite> select * from cats_db.db;

############# option3 : .open 'Tweet_Data.db'#######
# Default for sqlite is to use transient in-memory db, But
# We will create db using sqlite> .open db_name.db


--> 