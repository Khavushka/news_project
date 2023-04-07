'''
Python can generate random values. 
random numbers within a specified range;
a random choice from a range of items that are input

display a random integer between 1 and 100 inclusive. 
'''

import random

num = random.randint(0, 100)
print(num)


'''
display five colours and ask the user 
to pick one. if they pick the same as the program has choisen, say
"Well done", otherwise display a witty answer which involves the correct colour, e.g. "I bet you are Green with envy"
or " You are probably feeling Blue right now".
Ask them to guess again; if they have still not got it right, keep giving them the same clue and ask user to enter a colour until they guess it correctly.
'''

colour = random.choice(['green', 'yellow', 'red', 'pink', 'blue'])
user_choice = input('Pick one of this colour: ')
tryagain = True
while tryagain == True:
    theirchoice = input("Enter a colour: ")
    theirchoice = theirchoice.lower()
    if colour == theirchoice:
        print("Well done")
        tryagain = False
    else:
        if colour == "red":
            print("You are feeling Blue right now")
        elif colour == "green":
            print("You are Green right now")
        elif colour == "yellow":
            print("You are Yellow right now")
        elif colour == "pink":
            print("You are Purple right now")
        else: 
            print("Shame you are not feeling in the Blue, as you got it wrong!")