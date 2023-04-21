'''
CSV - stands for Comma Separated Values
'''

import csv

'''
Using the Books.csv file, ask the user how many records they want to add to the list and then allow them to add that many.
After all the data has been added, ask for an author and display all the books in the list by that author. 
If there are no books by that author in the list, display a suitable message.
'''
file = open("Books.csv", "w")
records = input("Please enter how many records, you want to add to the list: ")
file.write(records)
file.close()