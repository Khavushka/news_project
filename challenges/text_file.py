'''
open names.txt file. ask the user to input a new name. add this to the end of the file and display the entire file.
'''

# file = open("names.txt", "w")
# file.write("Hello\n")
# file.write("Hej\n")
# file.write("Hola\n")
# file.close()
# # print(file.read())

file = open("names.txt", "a")
user_input=input("Enter your name: ")
file.write(user_input + "\n")
file.close()

'''
display the following menu to the user:
1. create a new file 
2. dsiplay the file
3. add a new item to the file
make a selection 1, 2 or 3:
ask the user to enter 1, 2 or 3. If they select anything other than 1, 2 or 3 it should display a suitable error message.
if they select 1, ask the user to enter a school subject and save it to a new file. 
if they select 2, display the contects of the "Subject.txt" file.
if they select 3, ask the user to enter a new subject and save it to the file and then display the entire contents of the file.
run the program several times to test the options 
'''