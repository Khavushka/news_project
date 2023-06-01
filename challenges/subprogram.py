'''
Advantages:
- you can write a block of code and it can be used and reused at different times during the program
- it makes the program simpler to understand as the code is grouped together into chunks
'''

# def get_name():
#     user_name = input("Enter your name: ")
#     return user_name

# def print_Msg(user_name):
#     print("Hello", user_name)
    
# def main():
#     user_name = get_name()
#     print_Msg(user_name)
    
# main()

'''
Display the following menu to the user:
1. addition
2. subtraction
Enter 1 or 2:

if they enter 1, it should run a subprogram that will generate two random numbers between 5 and 20, and ask the user to add them together. Work out the correct answer and return both the user's answer and the correct answer. 

if they entered 2 as their selection on the menu, it should run a subprogram that will generate one number between 25 and 50 and another number between 1 and 25 and ask them to work out num1 minus num2. this way they will not have to worry about negative answers. return both the user's answer and the correct answer.

create another subprogram that will check if the user's answer matches the actual answer. if it does, display 'correct', otherwise display a message that will say 'incorrect, the answer is' and display the real answer.

if they do not select a relevant option on the first menu you should display a suitable message
'''
# import random

# # print("1.addition")
# # print("2.substraction")
# # input_user = int(input("Enter 1 or 2: "))
# def addition():
#     num1 = random.randint(5,20)
#     num2 = random.randint(5,20)
#     print(num1, "+", num2, "=")
#     user_answer = int(input("Your answer: "))
#     actual_answer = num1 + num2
#     answers = (user_answer, actual_answer)
#     return answers
        

# def substraction():
#     num1 = random.randint(25, 50)
#     num2 = random.randint(25, 50)
#     print(num1, "-", num2, "=")
#     user_answer = int(input("Your answer: "))
#     actual_answer = num1 - num2
#     answers = (user_answer, actual_answer)
#     return answers

# def check_answer(user_answer, actual_answer):
#     if user_answer == actual_answer:
#         print("Correct")
#     else:
#         print("incorrect, the answer", actual_answer)
    
# def main():
#     print("1) Addition")
#     print("2) Subtraction")
#     selection = int(input("Enter 1 or 2: "))
#     if selection == 1:
#         user_answer, actual_answer = addition()
#         check_answer(user_answer, actual_answer)
#     elif selection == 2:
#         user_answer, actual_answer = substraction()
#         check_answer(user_answer, actual_answer)
#     else:
#         print("Incorrect selection")
        
# main()

'''
create the following menu: 1. add to file, 2. view all records, 3. quit program
enter the number of your selection:

if the user selects 1, allow them to add to a file called Salaries.csv which will store their name and salary. If they select 2 it should display all records in the Salaries.csv file. If they select 3 it incorrect option they should see an error message. They should keep returning to the menu until they select option 3.
'''

# import csv

# def addto():
#     file = open('Salaries.csv', 'a')
#     name = input("Enter your name: ")
#     salary = int(input("Enter salary: "))
#     newRecords = name + ", " + str(salary) + ' kr'+ "\n"
#     file.write(str(newRecords))
#     file.close()

# def viewfile():
#     file = open('Salaries.csv', 'r')
#     for row in file:
#         print(row)
#     file.close()

# tryagain = True
# while tryagain == True:
#     print('1. add to file')
#     print('2. view all records')
#     print('3. quit program')
#     selection = input('Enter the number of your selection: ')
#     if selection == '1':
#         addto()
#     elif selection == '2':
#         viewfile()
#     elif selection == '3':
#         tryagain = False
#     else: 
#         print('Incorrect option')


'''
In Python, it is not technically possible to directly delete a record from a .csv file. Insted you need to save the file to a temporary list in Python, make the changes to the list and then overwrite the origib´nal fire with the temporary list. Then
Change the previous program to allow you to do this. Your menu should now look like this: 
1. add to file
2. view all records 
3. delete a record
4. quit program

Enter the number of your selection:
'''

import csv

def addTo():
    file = open('records.csv', 'a')
    name = input('Enter the name of the record: ')
    title = input('Enter title: ')
    record = int(input('Enter the year of record: '))
    newRecords = name + ' "' + title +'"' +  ' - ' + str(record) + '\n'
    file.write(str(newRecords))
    file.close()
    
def viewFile():
    file = open('records.csv', 'r')
    for row in file:
        print(row)
    file.close()

def deleteRecord():
    file = open('records.csv', 'r')
    x = 0
    tmpList = []
    for row in file:
        tmpList.append(row)
    file.close()
    for row in tmpList:
        print(x,row)
        x = x + 1
    rowToDelete = int(input('Enter records name: '))
    del tmpList[rowToDelete]
    file = open('records.csv', 'w')
    for row in tmpList:
        file.write(row)
    file.close()
        
tryagain = True
while tryagain == True:
    print('1. add to file')
    print('2. view all records')
    print('3. delete a record')
    print('4. quit program')
    selection = input('Enter the number of your selection: ')
    if selection == '1':
        addTo()
    elif selection == '2':
        viewFile()
    elif selection == '3':
        deleteRecord()
    elif selection == '4':
        tryagain = False
    else:
        print('Incorrect option')
    
        