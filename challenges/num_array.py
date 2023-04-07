'''
display an array of live numbers.
ask the user to select one of the numbers.
once they have selected a number, 
display the position of that item in the array.
if they enetr something that is not in the array, 
ask them to try again until they select a relevant item
'''
from array import *

live_numbers = ('i', [16, 9, 90, 3])
for i in live_numbers:
    print(i)
    
select_numbers = int(input("Select one of the numbers 16, 9, 90, 3: "))
    
print(live_numbers)