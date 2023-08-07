'''
create a program that will allow the user to create a new .csv file. it should ask them to enter the name and age of a person and then allow them to add this to the end of the file they have just created
'''

from tkinter import *

def create_new():
    name = textbox1.get()
    age = textbox2.get()
    message = name + age
    textbox3["text"] = message

window = Tk()
window.title("Program that will allow the user to create a new .csv")
window.geometry("400x250")

label_name = Label(text = "Enter your name:")
label_name.place(x = 30, y = 20)

textbox1 = Entry(text = "")
textbox1.place(x = 150, y = 20, width = 200, height = 25)

label_age = Label(text = "Enter age:")
label_age.place(x = 30, y = 50)

textbox2 = Entry(text = "")
textbox2.place(x = 150, y = 50, width = 200, height = 25)

textbox3 = Message(text = "")
textbox3.place(x = 150, y = 100, width = 200, height = 25)

window.mainloop()