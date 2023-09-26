'''
create a program that will allow the user to create a new .csv file. It should ask them to enter the name and age of a person and then allow them to add this to the end of the file they have just created.
'''

from tkinter import *
import csv

def add_to_list():
    person = person_box.get()
    if person:
        person_list.insert(END, person)
        person_box.delete(0, END)
        person_box.focus()
    else:
        person_box.delete(0, END)
        person_box.focus()
    

def clear_list():
    person_list.delete(0, END)
    person_box.focus()
    
def save_list():
    with open("person_list.csv", "w") as file:
        prs_list = person_list.get(0, END)
        item = 0
        for x in prs_list:
            newrecord = prs_list[item] + "\n"
            file.write(str(newrecord))
            item = item + 1
        file.close()
        

window = Tk()
window.title("Person list")
window.geometry("400x200")

label1 = Label(text="Enter a name and age:")
label1.place(x=20, y=20, width=130, height=25)

person_box = Entry(text=0)
person_box.place(x=150, y=20, width=100, height=25)
person_box.focus()

button1 = Button(text="Add to list", command=add_to_list)
button1.place(x=255, y=20, width=90, height=25)

person_list = Listbox()
person_list.place(x=20, y=60, width=330, height=100)

button2 = Button(text="Clear list", command=clear_list)
button2.place(x=250, y=170, width=100, height=25)

button3 = Button(text="Save list", command=save_list)
button3.place(x=120, y=170, width=100, height=25)

window.mainloop()
