'''
open names.txt file. ask the user to input a new name. add this to the end of the file and display the entire file.
'''

# file = open("names.txt", "w")
# file.write("Hello\n")
# file.write("Hej\n")
# file.write("Hola\n")
# file.close()
# # print(file.read())

# file = open("names.txt", "a")
# user_input=input("Enter your name: ")
# file.write(user_input + "\n")
# file.close()

'''
display the following menu to the user:
1. create a new file 
2. display the file
3. add a new item to the file
make a selection 1, 2 or 3:
ask the user to enter 1, 2 or 3. If they select anything other than 1, 2 or 3 it should display a suitable error message.
if they select 1, ask the user to enter a school subject and save it to a new file. 
if they select 2, display the contects of the "Subject.txt" file.
if they select 3, ask the user to enter a new subject and save it to the file and then display the entire contents of the file.
run the program several times to test the options 
'''

file = open("selection.txt", "w")
file.write("1,\n 2,\n 3")
file = open("selection.txt", "x")
user_select=input("Select 1, 2 or 3: ")
file.write(user_select, "\n")
file.close()