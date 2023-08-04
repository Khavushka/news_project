'''
1 kilometre = 0.6214 miles and 1 mile = 1.6093 kilometres. Using these figures, make a program, that will allow the user to convert between miles and kilometres
'''
from tkinter import *

def convert1():
    miles = mile_box.get()
    miles = int(miles)
    message = miles * 1.60934
    km_box.delete(0, END)
    km_box.insert(END, message)
    km_box.insert(END, " km")

def convert2():
    kilometer = km_box.get()
    kilometer = int(kilometer)
    message = kilometer * 0.6214
    mile_box.delete(0, END)
    mile_box.insert(END, message)
    mile_box.insert(END, " miles")
    
    
window = Tk()
window.title("Distance")
window.geometry("400x300")

label1 = Label(text = "Enter the value you want to convert:")
label1.place(x=20, y=20)

km_box = Entry(text = "")
km_box.place(x=30, y=50, width=200, height=25)
km_box["justify"] = "center"
km_box.focus()

convert1 = Button(text = "Convert miles to km", command = convert1)
convert1.place(x=30, y=80, width=200, height=25)

convert2 = Button(text = "Convert kilometers to mile", command=convert2)
convert2.place(x=30, y=110, width=200, height=25)

mile_box = Entry(text = "")
mile_box.place(x=30, y=140, width=200, height=25)
mile_box["justify"] = "center"

window.mainloop()