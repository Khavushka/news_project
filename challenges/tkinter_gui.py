'''
A GUI (graphical user interface) makes the program easier to use. It allows you, as the programmer, to create screens, text boxes and buttons to help nvigate through the program in a more user-friendly way. Tkinter is a library of features in Python that allows you to do this.
'''

from tkinter import *

def Call():
    msg = Label(window, text = 'You pressed the button')
    msg.place(x = 30, y = 50)
    button['bg'] = 'blue'
    button['fg'] = 'white'
    
window = Tk()
window.geometry(x = 30, y = 50)
button[bg] 