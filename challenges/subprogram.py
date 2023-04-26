'''
Advantages:
- you can write a block of code and it can be used and reused at different times during the program
- it makes the program simpler to understand as the code is grouped together into chunks
'''

def get_name():
    user_name = input("Enter your name: ")
    return user_name

def print_Msg(user_name):
    print("Hello", user_name)
    
def main():
    user_name = get_name()
    print_Msg(user_name)
    
main()

'''
Display the following menu to the user:
1. addition
2. subtraction
Enter 1 or 2:


'''