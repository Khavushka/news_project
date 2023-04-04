# ask for two numbers. If the first one is larger than the second, display the second number first and then the first number.
# otherwise show the first number first and then the second

# def two_number(one, two):
#     if one > two:
#         print('firts number bigger than first')
#     else:
#         print("second number ${two}")
#     return one, two

# one = int(input("Enter first number: "))
# two = int(input("Enter second number: "))

# print("Number {two_number} is bigger, than {two_number}")

one = int(input("Enter first number: "))
two = int(input("Enter second number: "))

if one > two:
    print("First number bigger")
else:
    print("Second number bigger")
    
'''
Ask the user to enter a number that is under 20. 
If they enter a number that is 20 or more, display the message.
"Too high", otherwise display "Thank you"
'''

user = int(input("Enter a number that is under 20: "))
if user > 20:
    print("Too high")
else:
    print("Thank you")
    