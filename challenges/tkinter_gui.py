'''
A GUI (graphical user interface) makes the program easier to use. It allows you, as the programmer, to create screens, text boxes and buttons to help nvigate through the program in a more user-friendly way. Tkinter is a library of features in Python that allows you to do this.
'''

# from tkinter import *

# def Call():
#     msg = Label(window, text = 'You pressed the button')
#     msg.place(x = 30, y = 50)
#     button['bg'] = 'pink'
#     button['fg'] = 'white'
    
# window = Tk()
# window.geometry('200x100')
# button = Button(text = 'Press me', command = Call)
# button.place(x = 30, y = 20, width=120, height=25)
# window.mainloop()

'''
Creates a window that will act as the display, referred to as 'window', adds a title and defines the size of the window
'''
# window = Tk()
# window.title("Window Title")
# window.geometry("450x100")

# adds text to the screen displaying the message
# label = Label(text = 'Salam XABA')

# creates a blank entry box. Entry boxes can be used by the user to input data or used to display output
#entry_box = Entry(text = 0)

'''
Create a window that will ask the user to enter their name. When they click on a button it should display the message "Hello" and their name and change the background colour and font colour of the message box.
'''

# def userCall():
#     msg = Label(window, text='Enter your name: ')
#     msg.place(x = 30, y = 50)
#     button['bg'] = 'yellow'
#     button['fg'] = 'green'
    
# window = Tk()
# window.geometry('200x100')
# button = Button(text = 'Hello', command = userCall)
# button.place(x = 30, y = 20, width = 120, height = 25)
# window.mainloop()


'''
Create a window that will ask the user to enter their name. When they click on a button it should display the message "Hello2 and their name and change the background colour and font colour of the message box
'''
# from tkinter import *

# def click():
#     name = textbox1.get()
#     email = textbox3.get()
#     message = "Hello " + name + " " + email
#     textbox2["bg"] = "red" 
#     textbox2["fg"] = "green" 
#     textbox2["text"] = message
    
# window = Tk()
# window.geometry("500x300")

# label1 = Label(text = "Enter your name: ")
# label1.place(x = 30, y = 20)

# textbox1 = Entry(text = "")
# textbox1.place(x = 150, y = 20, width = 200, height = 25)
# textbox1["justify"] = "center"
# textbox1.focus()

# label3 = Label(text = "Enter your email: ")
# label3.place(x = 30, y = 50)

# textbox3 = Entry(text="")
# textbox3.place(x = 150, y = 50, width = 200, height = 25)
# textbox3["justify"] = "center"
# textbox3.focus()

# button1 = Button(text = "Press me", command = click)
# button1.place(x=30, y=100, width=120, height=25)

# textbox2 = Message(text = "")
# textbox2.place(x = 150, y = 100, width = 200, height = 150)
# textbox2["bg"] = "white"
# textbox2["fg"] = "black"

# window.mainloop()

'''
My Tkinter calculation
'''
from tkinter import *

def click():
    userInput1 = cifra1.get()
    userInput2 = cifra2.get()
    choose = textbox3.get()
    message = "This is result: " + userInput1 + choose + userInput2
    pressbutton["bg"] = "red"
    pressbutton["fg"] = "green"
    pressbutton["text"] = message

def main(userInput1, userInput2, choose):
    if choose == "+":
        samlet = userInput1 + userInput2
    elif choose == "-":
        samlet = userInput1 - userInput2
    elif choose == "*":
        samlet = userInput1 * userInput2
    elif choose == "/":
        samlet = userInput1 / userInput2
    else:
        return choose
    return samlet

# result = main(userInput1, userInput2, choose)
# print("This is: ", result)
    
window =Tk()
window.geometry("500x300")

label1 = Label(int(input("Enter first: ")))
label1.place(x = 30, y = 20)
cifra1 = Entry(text = "")
cifra1.place(x = 150, y = 20, width = 200, height = 25)
cifra1["justify"] = "center"
cifra1.focus()

label2 = Label(int(input("Enter second: ")))
label2.place(x = 30, y = 20)
cifra2 = Entry(text="")
cifra2.place(x = 150, y = 50, width = 200, height = 25)
cifra2["justify"] = "center"
cifra2.focus()

label3 = Label(input("+, -, *, /: "))
label3.place(x = 30, y = 20)
textbox3 = Entry(text="")
textbox3.place(x = 150, y = 50, width = 200, height = 25)
textbox3["justify"] = "center"
textbox3.focus()

pressbutton = Button(text = "Press me", command = click)
pressbutton.place(x=30, y=100, width=120, height=25)

textbox4 = Message(text = "")
textbox4.place(x = 150, y = 100, width = 200, height = 150)
textbox4["bg"] = "white"
textbox4["fg"] = "black"

# userInput1 = int(input("Enter first: "))
# userInput2 = int(input("Enter second: "))
# choose = input("+, -, *, /: ")


window.mainloop()