from tkinter import *
import csv

def add_to_list():
    num1 = int(num_box1.get())
    num2 = int(num_box2.get())
    result = num1 + num2
    result_str = f"{num1} + {num2} = {result}"
    num_box1.delete(0, END)
    num_box2.delete(0, END)
    num_box1.focus()
    num_list.insert(END, result_str)

def plus():
    num1 = int(num_box1.get())
    num2 = int(num_box2.get())
    result = num1 + num2
    result_str = f"{num1} + {num2} = {result}"
    num_box1.delete(0, END)
    num_box2.delete(0, END)
    num_box1.focus()
    num_list.insert(END, result_str)

def substraction():
    num1 = int(num_box1.get())
    num2 =int(num_box2.get())
    result = num1 - num2
    result_str = f"{num1} - {num2} = {result}"
    num_box1.delete(0, END)
    num_box2.delete(0, END)
    num_box1.focus()
    num_list.insert(END, result_str)

def multiple():
    num1 = int(num_box1.get())
    num2 = int(num_box2.get())
    result = num1 * num2
    result_str = f"{num1} * {num2} = {result}"
    num_box1.delete(0, END)
    num_box2.delete(0, END)
    num_box1.focus()
    num_list.insert(END, result_str)

def division():
    num1 = num_box1.get()
    num2 = num_box2.get()
    result = num1 / num2
    result_str = f"{num1} / {num2} = {result}"
    num_box1.delete(0, END)
    num_box2.delete(0, END)
    num_box1.focus()
    num_list.insert(END, result_str)

def clear_list():
    num_list.delete(0, END)
    num_box1.focus()

def save_list():
    with open("calculator.csv", "w") as file:
        tmp_list = num_list.get(0, END)
        for x in tmp_list:
            file.write(f"{x}\n")

window = Tk()
window.title("My Tkinter calculator")
window.geometry("600x300")

label1 = Label(text="Enter first number:")
label1.place(x=20, y=20, width=120, height=25)

num_box1 = Entry()
num_box1.place(x=150, y=20, width=100, height=25)
num_box1.focus()

button1 = Button(text="+", command=plus)
button1.place(x=270, y=20, width=30, height=25)

button2 = Button(text="-", command=substraction)
button2.place(x=310, y=20, width=30, height=25)

button3 = Button(text="*", command=multiple)
button3.place(x=350, y=20, width=30, height=25)

button4 = Button(text="/", command=division)
button4.place(x=390, y=20, width=30, height=25)

label2 = Label(text = "Enter second number:")
label2.place(x=20, y=60, width=140, height=25)

num_box2 = Entry()
num_box2.place(x=150, y=60, width=100, height=25)

add_button = Button(text="Add", command=add_to_list)
add_button.place(x=270, y=60, width=50, height=25)

num_list = Listbox()
num_list.place(x=20, y=90, width=400, height=100)

button5 = Button(text ="Clear list", command=clear_list)
button5.place(x=270, y=250, width=100, height=25)

button6 = Button(text="Save list", command = save_list)
button6.place(x=150, y=250, width=100, height=25)

window.mainloop()