'''
save several images in the same folder as your program and call them 1.gif, 2.gif, 3.gif, etc. make sure they are all .gif files. display one in a window and ask the user to enter a number. it should then use that number to choose the correct file name and display the correct image.
'''

from tkinter import *

def clicked():
    pass

window = Tk()
window.title("GIF")
window.geometry("400x400")


art = PhotoImage(file = r"challenges\tkinter\logo.gif")
photobox = Label(window, image = art)
photobox.image = art
photobox.place(x=100, y=20, width=200, height=150)

label = Label(text = "Select Art number:")
label.place(x=50, y=200, width=100, height=25)

selection = Entry(text="")
selection.place(x=200, y=200, width=100, height=25)
selection.focus()

button = Button(text="See Art", command = clicked)
button.place(x=150, y=250, width=100, height=25)

mainloop()