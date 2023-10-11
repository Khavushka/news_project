'''
using the Bookinfo database, ask the user for an author's name and then save all the books by that author to a text file, with each field separated by dashes so it looks as follows:
    5. Murder on the Orient Express - Agatha Christie - 1934
    8. The murder on the links - Agatha Christie - 1923
    10. The secret adversary - Agatha Christie - 1921
    11. The seven dials mystery - Agatha Christie - 1929
    
Open the text file to make sure it has worked correctly.
'''

import sqlite3

with sqlite3.connect(r"db\Bookinfo.db") as db:
    cursor = db.cursor()
    
cursor.execute("""SELECT Authors from Author""")
for x in cursor.fetchall():
    print(x)

db.close()