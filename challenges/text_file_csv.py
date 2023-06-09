'''
CSV - stands for Comma Separated Values
'''

import csv

'''
Using the Books.csv file, ask the user how many records they want to add to the list and then allow them to add that many.
After all the data has been added, ask for an author and display all the books in the list by that author. 
If there are no books by that author in the list, display a suitable message.
'''
records = int(input("How many books you want to add to the list?  "))
file = open("Books.csv", "a")

for info in range(0, records):
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year: ")
    newrecord = title + ", " + author + ", " + year + "\n"
    file.write(str(newrecord))
file.close()


fileSearch = input("Search after book: ")
file = open("Books.csv", "r")
count = 0
for book in file:
    if fileSearch in str(book):
        print(book)
if count == 0:
        print("There are no books by that author in the list.")
file.close()


filename = "Books.csv"
row_number = int(input("Enter book you wanted to delete from the list: "))

with open(filename, "r") as file:
    rows = file.readlines()

# Remove the specified row from the list
if row_number < len(rows):
    del rows[row_number]

with open(filename, "w") as file:
    for row in rows:
        file.write(row)