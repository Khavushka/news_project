'''
create an SQL database called PhoneBook that contains  a table called Names with the following data
'''
import sqlite3

with sqlite3.connect(r"db\PhoneBook.db") as db:
    cursor = db.cursor()
    
cursor.execute("""CREATE TABLE IF NOT EXISTS Names (
    id integer PRIMARY KEY,
    firstname text,
    surname text,
    phonenumber text);""")

cursor.execute(""" INSERT INTO Names (id, firstname, surname, phonenumber) 
               VALUES("4", "Howels", "Phillips", "01954 395773")""")
db.commit()

cursor.execute(""" INSERT INTO Names (id, firstname, surname, phonenumber) 
               VALUES("5", "Karen", "Phillips", "01954 295773")""")
db.commit()

cursor.execute(""" INSERT INTO Names (id, firstname, surname, phonenumber) 
               VALUES("6", "Anne", "Phillips", "01954 495773")""")
db.commit()

db.close()