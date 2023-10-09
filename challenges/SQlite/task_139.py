'''
create an SQL database called PhoneBook that contains  a table called Names with the following data
'''
import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()
    
cursor.execute("""CREATE TABLE IF NOT EXISTS Names (
    id integer PRIMARY KEY,
    firstname text,
    surname text,
    phonenumber text);""")

cursor.execute(""" INSERT INTO Names (id, firstname, surname, phonenumber) 
               VALUES("1", "Howels", "Phillips", "01954 395773")""")
db.commit()

cursor.execute(""" INSERT INTO Names (id, firstname, surname, phonenumber) 
               VALUES("2", "Karen", "Phillips", "01954 295773")""")
db.commit()

cursor.execute(""" INSERT INTO Names (id, firstname, surname, phonenumber) 
               VALUES("3", "Anne", "Phillips", "01954 495773")""")
db.commit()

db.close()