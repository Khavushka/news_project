'''
create your own that consists of several vertical multi-coloured lines. creates a logo which measures 200 x 150. using Paint or another graphics package. create the following window using your own icon and logo

when the user enters their name and clicks on the Press Me button it should display "Hello" and their name in the second text box
'''

from tkinter import *

def add_to_second():
    name = name_box1.get()
    result = f"Hello  {name}"
    name_list.insert(END, result)

window = Tk()
window.title("More Tkinter")
window.configure(background="blue")
window.wm_iconbitmap(r"challenges\tkinter\stripes.ico")
window.geometry("600x300")

label1 = Label(text="Enter your name:")
label1.place(x=20, y=20, width=120, height=25)

name_box1 = Entry()
name_box1.place(x=150, y=20, width=100, height=25)
name_box1.focus()

button1 = Button(text="Press Me", command=add_to_second, bg='white', fg='blue')
button1.place(x=270, y=20, width=100, height=25)

name_list =Listbox()
name_list.place(x=20, y=90, width=200, height=100)

window.mainloop()