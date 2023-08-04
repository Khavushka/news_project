'''
1 kilometre = 0.6214 miles and 1 mile = 1.6093 kilometres. Using these figures, make a program, that will allow the user to convert between miles and kilometres
'''
from tkinter import *

def converter():
    kilometer = km_box.get()
    mile = miles_box.get()
    
window.Tk()
window.title("Converter between miles and kilometres")
window.geometry("400x300")

label = Label(text = "Enter kilometer:")
label.place(x=20, y=20, width=100, height=100)

km_box = Entry(text = "")
km_box.place(x=120, y=20, width=100, height=25)
km_box.focus()

conveter_to = Button(text="Convert", command=converter)
conveter_to.place(x=250, y=20, width=100, height=100)