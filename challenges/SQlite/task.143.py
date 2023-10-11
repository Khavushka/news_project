'''
using the Bookinfo database, ask the user to enter year and display all the books published after that year, sorted by the year they were published.
'''

import sqlite3

with sqlite3.connect(r"db\Bookinfo.db") as db:
    cursor = db.cursor()
    
cursor.execute("SELECT *FROM Authors")
for x in cursor.fetchall():
    print(x)
print("---------")
    
selectid = int(input("Enter id: "))
print()

cursor.execute("""SELECT Authors.id, Authors.Bookname, Authors.Author FROM Authors WHERE id>? ORDER BY id""", [selectid])
for x in cursor.fetchall():
    print(x)
    
db.close()