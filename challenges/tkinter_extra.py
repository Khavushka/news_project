'''
create a program that will ask the user to enter a number in a box. when they click on a button it will add that number to a total and display it in another box. this can be repeated as many times as they want and keep adding to the total. there should be another button that resets the total back to 0 and empties the original text box, ready for them to start again.
'''

# from tkinter import *

# def click():
#     user_enter = int(input1.get())
#     btn["bg"] = "red"
#     message = user_enter
#     textbox1["text"] = message
    

# window= Tk()
# window.geometry("500x400")

# label1 = Label(text = "Enter a number: ")
# label1.place(x = 30, y = 40)

# input1 = Entry(text = "")
# input1.place(x = 150, y = 40, width = 200, height = 25)
# input1["justify"] = "center"
# input1.focus()

# btn = Button(text = "Result", command = click)
# btn.place(x = 30, y = 160, width = 120, height = 25)

# textbox1 = Message(text = "")
# textbox1.place(x = 150, y = 160, width = 200, height = 100)
# textbox1["bg"] = "white"
# textbox1["fg"] = "black"

# window.mainloop()

from tkinter import *

def add_on():
    num = enter_txt.get()
    num = int(num)
    answer = output_txt["text"]
    answer = int(answer)
    total = num + answer
    output_txt["text"] = total
    
def reset():
    total = 0
    output_txt["text"] = 0
    enter_txt.delete(0, END)
    enter_txt.focus()

total = 0
num = 0

window = Tk()
window.title("Adding Together")
window.geometry("450x100")

enter_lbl = Label(text = "Enter a number:")
enter_lbl.place(x = 50, y = 20, width = 100, height = 25)

enter_txt = Entry(text = 0)
enter_txt.place(x = 150, y = 20, width = 100, height = 25)
enter_txt["justify"] = "center"
enter_txt.focus()

add_btn = Button(text = "Add", command = add_on)
add_btn.place(x = 300, y = 20, width = 50, height = 25)

output_lbl = Label(text = "Answer = ")
output_lbl.place(x = 50, y = 50, width = 100, height = 25)

output_txt = Message(text = 0)
output_txt.place(x = 150, y = 50, width = 100, height = 25)
output_txt["bg"] = "white"
output_txt["relief"] = "sunken"

clear_btn = Button(text = "Clear", command = reset)
clear_btn.place(x = 300, y = 50, width = 50, height = 25)

window.mainloop()

'''
create a window that will ask the user to enter a name in a text box. when they click on a button it will add it to the end of the list that is displayed on the screen. create another button which will clear the list.
'''

def ent_name():
    name = textbox1.get()
    message = "Hello " + name
    textbox2["text"] = message
    
def reset_name():
    textbox1.delete(0, END)
    textbox1.focus()
    
window = Tk()
window.title("Name list")
window.geometry("450x400")

label1 = Label(text = "Enter your name: ")
label1.place(x = 30, y = 40)

textbox1 = Entry(text = "")
textbox1.place(x = 150, y = 40, width = 200, height = 25)

button1 = Button(text = "Press", command = ent_name)
button1.place(x = 30, y = 100, width = 120, height = 25)

textbox2 = Message(text = "")
textbox2.place(x = 150, y = 100, width = 120, height = 150)

clear_button = Button(text = "Clear", command = reset)
clear_button.place(x = 300, y = 120, width = 50, height = 25)

window.mainloop()