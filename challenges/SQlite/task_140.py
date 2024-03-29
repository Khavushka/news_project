"""
using the PhoneBook database from program 139, write a program that will display the following menu:
1. View phone book
2. Add to phone book
3. Search for surname
4. Delete person from phone book
5. Quit

- if the user selects 1, they should be able to view the entire phonebook. 
- if they select 2, it should allow them to add a new person to the phonebook, 
- if they select 3, it shoukd ask them for a surname and then display only the records of people with the same surname. 
- if they select 4, it should ask for an ID and then delete that record from the table. 
- if they select 5, it should end the program. finally, it should display a suitable message if they enter an incorrect seelction from the menu. they should return to the menu after each action, until they select 5.
"""

import sqlite3

def viewphonebook():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    
def addtophonebook():
    newid = int(input("Enter ID: "))
    newfname = input("Enter first name: ")
    newsname = input("Enter surname: ")
    newpnum = input("Enter phone number: ")
    cursor.execute("""INSERT INTO Names (id,firstname,surname,phonenumber) VALUES (?,?,?,?)""", (newid, newfname, newsname, newpnum))
    db.commit()
    
def selectname():
    selectsurname = input("Enter a surname: ")
    cursor.execute("SELECT * FROM Names WHERE surname = ?", [selectsurname])
    for x in cursor.fetchall():
        print(x)
            
def deletedata():
    selectid = int(input("Enter ID: "))
    cursor.execute("DELETE FROM Names WHERE id = ?", [selectid])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()
    
with sqlite3.connect(r"db\PhoneBook.db") as db:
    cursor = db.cursor()
    
def main():
    again = "y"
    while again == "y":
        print()
        print("Main Menu")
        print()
        print("1. View phone book")
        print("2. Add to phone book")
        print("3. Search for surname")
        print("4. Delete person from phone book")
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