'''
change a program, so that when a new name and gender is added to the list box it is also written to a text file. add another button that will display the entire text file in the main Python shell window.
'''

from tkinter import *

def add_to_list():
    name = textbox1.get()
    textbox1.delete(0, END)
    genderselect = label2.get()
    newdata = name + ", " + genderselect + "\n"
    name_list.insert(END, newdata)
    textbox1.focus()
    file = open("people_names.txt", "a")
    file.write(newdata)
    file.close()
    
def display_file():
    file = open("people_names.txt", "r")
    print(file.read())

window = Tk()
window.title("People list")
window.geometry("450x400")
# window.configure(background="light blue")


label1 = Label(text="Enter name:")
label1.place(x=50, y=50, width=100, height=25)
textbox1 =Entry(text="")
textbox1.place(x=150, y=50, width=150, height=25)
textbox1["justify"] = "center"
textbox1.focus()

label_gender = Label(text="Select the gender")
label_gender.place(x=50, y=100, width=100, height=25)
label2 = StringVar(window)
label2.set("M/F")
option_list =OptionMenu(window, label2, "M", "F")
option_list.place(x=150, y=100)

name_list = Listbox()
name_list.place(x=150, y=150, width=150, height=100)

addbtn = Button(text = "Add to list", command = add_to_list)
addbtn.place(x=50, y=300, width=100, height=25)

display_text = Button(text = "Display file", command = display_file)
display_text.place(x=160, y=300, width=100, height=25)

mainloop()