'''
- changed the icon on the title bar
- changed the background colour of the main window
- added a static image of the logo to the top left, which will not change
- created a label which, at the moment, displays "Hello";
- added a Click Me button
- added a drop down option entitled Select Name, which will display three names; "Bob", "Sue", "Tim" to the user;
- added a second image in the lower half of the window which will change to show the photograph of the person selected from the drop-down list when the user clicks on the Click Me button.
'''
import tkinter as tk

window = tk.Tk()
window.title("My Window")
window.geometry("600x500")

# Define global variables for images
logo = tk.PhotoImage(file=r"challenges\tkinter\logo.gif")
bob_image = tk.PhotoImage(file=r"challenges\tkinter\logo.gif")
sue_image = tk.PhotoImage(file=r"challenges\tkinter\logo.gif")
tim_image = tk.PhotoImage(file=r"challenges\tkinter\logo.gif")

# Function to update the displayed image
def update_image():
    sel = selectName.get()
    mesg = "Hello " + sel
    mlabel["text"] = mesg

    if sel == "Bob":
        photobox["image"] = bob_image
    elif sel == "Sue":
        photobox["image"] = sue_image
    elif sel == "Tim":
        photobox["image"] = tim_image
    else:
        photobox["image"] = logo

# Set the window icon
window.wm_iconbitmap(r"challenges\tkinter\stripes.ico")

# Set the background color
window.configure(background="light green")

# Create a label for displaying text
mlabel = tk.Label(window, text="")
mlabel.pack()

# Create an option menu
selectName = tk.StringVar(window)
selectName.set("Select Name")
nameList = tk.OptionMenu(window, selectName, "Bob", "Sue", "Tim", command=update_image)
nameList.pack()

# Create a label for displaying images
photobox = tk.Label(window, image=logo)
photobox.pack()

window.mainloop()
