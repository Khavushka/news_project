'''
Create a program that will ask the user to enter a name and then select the gender for that person from a drop-down list. It should then add the name and the gender (separated by a comma) to alist box when the user clicks on a button
'''

from tkinter import *

def click():
    name = textbox1.get()
    gender = 

window = Tk()
window.title("drop down list")
window.geometry("450x400")
# window.configure(background="light blue")


label1 = Label(text="Enter name:")
label1.place(x=30, y=20, width=100, height=25)

textbox1 =Entry(text="")
textbox1.place(x=150, y=20, width=200, height=25)
textbox1["justify"] = "center"
textbox1.focus()

label_gender = Label(text="Select the gender:")
label_gender.place(x=50, y=100, width=100, height=25)
label2 = StringVar(window)
label2.set("M/F")
option_list =OptionMenu(window, label2, "one", "two", "tre")
option_list.place(x=150, y=100)

name_list = Listbox()
name_list.place(x=150, y=150, width=150, height=100)

# ZIP - function to iterate two or more parallel
# first = [1, 2, 3]
# second= ['a', 'b', 'c']

# for x, y in zip(first, second):
#     print(x, y)

mainloop()