'''
set the total to 0 to start with. While the total is 50 or less, 
ask the user to input a number. Add that number to the total and print 
the message "The total is...[total]".
stop the loop when the total is over 50
'''

# total = 0
# while total <= 50:
#     user = int(input("Enter a number: "))
#     total = total + user
#     print(total)
    

'''
create a variable called compnum and set the value to 50.
ask the user to enter a number.
while their guess is not the same as the compnum value.
tell them if their guess is too low or too high and ask them to have another guess.
if they enter the same value as compnum, display the message
"Well done, you took [count] attempts"
'''

compnum = 50
user_ask = int(input("Enter a number: "))
count = 1
while user_ask != compnum:
    if user_ask < compnum:
        print("Too low")
    else:
        print("Too high")
    count = count + 1
    user_ask = int(input("Have another guess: "))  
print("Well odne, you took", count, " attempts")
        