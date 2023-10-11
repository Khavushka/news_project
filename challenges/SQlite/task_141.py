'''
create a new SQL database called Bookinfo that will store a list of authors the books they wrote. it will have two tables. the first one should be called Authors and contain the following data.
the second should be called Books and contain the following data.
'''

import sqlite3

def viewphonebook():
    cursor.execute("SELECT * FROM Authors")
    for x in cursor.fetchall():
        print(x)
    
def addtophonebook():
    newid = int(input("Enter ID: "))
    newfname = input("Enter book name: ")
    newsname = input("Enter Author: ")
    cursor.execute("""INSERT INTO Authors(id,Bookname,Author) VALUES (?,?,?)""", (newid, newfname, newsname))
    db.commit()
    
def selectname():
    selectsurname = input("Enter a surname: ")
    cursor.execute("SELECT * FROM Authors WHERE Author = ?", [selectsurname])
    for x in cursor.fetchall():
        print(x)
            
def deletedata():
    selectid = int(input("Enter ID: "))
    cursor.execute("DELETE FROM Authors WHERE id = ?", [selectid])
    cursor.execute("SELECT * FROM Authors")
    for x in cursor.fetchall():
        print(x)
    db.commit()


with sqlite3.connect(r"db\Bookinfo.db") as db:
    cursor = db.cursor()
    
cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
    id integer PRIMARY KEY,
    Bookname text,
    Author text);""")

# cursor.execute("""INSERT INTO Authors(id, Bookname, Author)Values("567, Dublin, J.K.Rowling")""")
    
def main():
    again = "y"
    while again == "y":
        print()
        print("Main Menu")
        print()
        print("1. View book")
        print("2. Add a book")
        print("3. Search a book")
        print("4. Delete a book")
        print("5. Quit")
        print()
        selection = int(input("Enter your selection: "))
        print()
        
        if selection == 1:
            viewphonebook()
        elif selection == 2:
            addtophonebook()
        elif selection == 3:
            selectname()            
        elif selection == 4:
            deletedata()
        elif selection == 5:
            again = "n"
        else:
            print("Incorrect selection entered")
            
main()
db.close()