# the first line of the program to allow Python to use the SQLite3 library
import sqlite3

# connects to the company database. If no such database exists, it will create one. The file will be stored in the same folder as the program.
with sqlite3.connect("company.db") as db:
    cursor=db.cursor()
    

# creates a table called employees which has four fields (id, name, dept and salary). It specifies the data type for each field, defines which field is the primary key and which fields cannot be left blank. The triple speech marks allow the code to be split over several lines to make it easier to read rather than having it all displayed in one line.

cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
    id integer PRIMARY KEY,
    name text NOT NULL,
    dept text NOT NULL,
    salary integer);""")

# Inserts data into the employees table. The db.commit() line saves the changes.
cursor.execute("""INSERT INTO employees (id, name, dept, salary)
               VALUES("1","Bob", "Sales","25000")""")
db.commit()

# allows a user to enter new data which is then inserted into the table
newID = input("Enter ID number: ")
newName = input("Enter name: ")
newDept = input("Enter department: ")
newSalary = input("Enter salary: ")
cursor.execute("""INSERT INTO employees(id, name, dept, salary)
               VALUES(?,?,?,?)""", (newID, newName, newDept, newSalary))
db.commit()

# displays all the data from the employees table
cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())

# this must be the last line in the program to close the database
db.close()