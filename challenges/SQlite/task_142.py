'''
using the Bookinfo database from program 141, display the list of authors and their place of birth. ask the user to enter a place of birth and then show the title, date published and autor's name for all the books by authors who ere born in the location they selected
'''
import sqlite3

with sqlite3.connect(r"db\Bookinfo.db") as db:
    cursor = db.cursor()
    
cursor.execute("SELECT * FROM Authors")
for x in cursor.fetchall():
    print(x)
    
print()
location = input("Enter a Authors name: ")
print()

cursor.execute("""SELECT Authors.id, Authors.Bookname, Authors.Author
FROM Authors
WHERE Authors.Author = ?;""", [location])
for x in cursor.fetchall():
    print(x)
    
db.close()