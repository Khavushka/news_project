'''
Create a window that will ask the user to enter a number in a text box. when they click on a button it will use the code variable.isdigit() to check to see if it is a whole number. if it is a whole number, add it to a list box. add another button that will clear the list
'''

from tkinter import *

def is_dig():
    num = textbox1.get()
    if num.isdigit():
        textbox2.insert(END, num)
        textbox1.delete(0, END)
        textbox1.focus()
    else:
        textbox1.delete(0, END)
        textbox1.focus()
    
def reset_button():
    textbox2.delete(0, END)
    textbox1.focus()
    
def save():
    pass

window = Tk()
window.title("GUI")
window.geometry("400x250")

label1 = Label(text = "Enter a number:")
label1.place(x = 20, y = 20)

textbox1 = Entry(text = 0)
textbox1.place(x = 120, y = 20, width = 100, height = 25)
textbox1.focus()

button1 = Button(text = "Click", command = is_dig)
button1.place(x = 230, y = 20, width = 100, height = 25)

label2= Label(text = "List of numbers:")
label2.place(x = 20, y = 50)

textbox2 = Listbox()
textbox2.place(x = 120, y = 50, width = 100, height = 100)

clear_button = Button(text ="Clear", command = reset_button)
clear_button.place(x = 230, y = 50, width = 100, height = 25)

save_button = Button(text = "Save to .csv file", command = save)
save_button.place(x = 230, y = 80, width = 100, height = 25)

window.mainloop()