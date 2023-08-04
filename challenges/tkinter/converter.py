'''
1 kilometre = 0.6214 miles and 1 mile = 1.6093 kilometres. Using these figures, make a program, that will allow the user to convert between miles and kilometres
'''
from tkinter import *

def converter():
    kilometer = km_box.get()
    kilometer = int(kilometer)
    message = kilometer * 0.6214
    
    
window = Tk()
window.title("Distance")
window.geometry("400x300")

label = Label(text = "Enter kilometer:")
label.place(x=20, y=20)

km_box = Entry(text = "")
km_box.place(x=30, y=50, width=200, height=25)
km_box.focus()

convert1 = Button(text="Convert miles to km", command=convert1)
convert1.place(x=30, y=80, width=200, height=25)

convert2 = Button(text = "Convert kilometers to mile", command=convert1)


window.mainloop()