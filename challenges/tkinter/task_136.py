'''
Create a program that will ask the user to enter a name and then select the gender for that person from a drop-down list. It should then add the name and the gender (separated by a comma) to alist box when the user clicks on a button
'''

from tkinter import *

def click():
    pass

window = Tk()
window.title("drop down list")
window.geometry("450x400")
window.configure(background="light blue")


label1 = Label(text="Enter name:")
label1.place(x=30, y=20, width=100, height=25)

textbox1 =Entry(text="")
textbox1.place(x=150, y=20, width=200, height=25)
textbox1["justify"] = "center"
textbox1.focus()

label2 = Label(text="Select tehe gender:")
label2.place(x=30, y=60, width=120, height=25)



# ZIP - function to iterate two or more parallel
# first = [1, 2, 3]
# second= ['a', 'b', 'c']

# for x, y in zip(first, second):
#     print(x, y)

mainloop()