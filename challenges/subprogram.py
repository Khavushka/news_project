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

if they enter 1, it sholud run a subprogram that will generate two random numbers between 5 and 20, and ask the user to add them together. Work out the correct answer and return both the user's answer and the correct answer. 

if they entered 2 as their selection on the menu, it should run a subprogram that will generate one number between 25 and 50 and another number between 1 and 25 and ask them to work out num1 minus num2. this way they will not have to worry about negative answers. return both the user's answer and the correct answer.

create another subprogram that will check if the user's answer matches the actual answer. if it does, display 'correct', otherwise display a message that will say 'incorrect, the answer is' and display the real answer.

if they do not select a relevant option on the first menu you should display a suitable message
'''

def addition():
    user_name = input("Enter your name: ")
    return user_name

def substraction(user_name):
    print("Hello", user_name)
    
def main():
    user_name = addition()
    substraction(user_name)
    
main()
