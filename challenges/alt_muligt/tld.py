'''
create an empty list called "nums"
ask the user to enter numbers
atter each number is entered, add it to the end of the nums list and display the list.
once they have entered three numbers, ask them if they still want the last number they entered saved.
if they say "no", remove the last item from the list. 
display the list of numbers.
'''

# nums = []
# count = 0
# while count < 3: 
#     user = int(input("Enter a number: "))
#     nums.append(user)
#     print(nums)
#     count = count + 1
# print(nums)


'''
ask the user to enter a new password.
ask them to enter it again. 
if the two passwords match, display "Thank you"
if the letters are correct but in the wrong case, 
display the message "They must be in the same case".
otherwise display the message "Incorrect".
'''

user_password = input("Enter a new password: ")
user_password1 = input("Enter it again: ")
if user_password == user_password1:
    print("Thank you")
elif user_password.lower() == user_password1.lower():
    print("They must have the same password")
else:
    print("Incorrect")
