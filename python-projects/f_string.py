# with  in f-strings debugging, you can also perform math operations

'''
the first one is the debug feature with f-strings.
instead of writing out "variable = ' '  ", do {variable = } instead.
this saves a lot of time and effort, as well as makes your code look cleaner. within f-strings debugging, you can also perform math operations  in the last line.
'''

# 1. Debug mode
print("---------------------Debug mode")
x = 10
y = 20

print(f"x ={x}, y = {y}")
print(f"{x = }, {y =}")

# math operations
print(f"{ x * y = }")

#  2. Number formatting 
'''
there are various formatting/conversions you can perform with strings. the following are done below
- set decimal places :.nf where n is the number of decimal places
- hex conversion
- binary conversion
- octal conversion
- scientific notation
- pad number with leading zeros :0n where n is the total number of characters
'''

print("-----------------Number formatting")

number = 420

# decimal places 
print(f"number: {number:.2f}")

#  hex converion 
print(f"hex: {number:#0x}")

#  binary conversion
print(f"binary: {number:b}")

# octal conversion
print(f"octal: {number:o}")

#  scientific notation
print(f"scientific: {number:o}")

#  total number of characters
print(f"Number: {number:09}\n")

'''
let's say you have a large number, as large as Apple's market cap; you can use :, where , is the separator or, if you want f string out a percentage value, you can use :.2% telling Python to set 2 decimal places and add a percentage sign to the end of the string. 
'''
apple_marketcap = 2.626 * 10e12
print(f"{apple_marketcap = :,}")

percentage = 10.394394
print(f"{percentage = :.2%}\n")


'''
Date formatting
- no microseconds
- date only
- time only
- time with AM/PM
- 24-hour format
'''
print("-----------------------Date formatting")

import datetime

today = datetime.datetime.utcnow()
print(f"datetime: {today}\n")

print(f"date time: {today:%m/%d/%Y  %H:%M:%S.%f}")
print(f"date: {today:%m/%d/%Y}")
print(f"time: {today:%H:%M:%S.%f}") 
print(f"time: {today:%H:%M:%S %p}") 
print(f"time: {today:%H:%M}\n")

# locale's appropriate date and time representation
print(f"locale appropriate: {today:%c}")

# weekday
print(f"weekday: {today:%A}")

# day of the year
print(f"day of year: {today:%j}")

# how far are we into the year?
day_of_year = f"{today:%j}"
print(f"prograss % year: {int(day_of_year)/365 * 100:.2f}%")

'''
4. Repr&str
if you write OOP in Python, you'd be familiar with the dunder methods __repr__ and __str__ 
the basic idea is:
__repr__=developer friendly
__str__= user friendly
Below is an example of a dataclass Person with name and age attributes. For a dataclass, by default (without a str method defined), printing the object will give you the output of repr. 

With a str the method defined, you'd need to write !r to tell Python to print out the repr method instead.
'''

print("--------------------Repr&str")

from dataclasses import dataclass 

@dataclass 
class Person:
    name : str
    age : int
    
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"
    
Eva = Person("Eva E.", 51)
print(f"{Eva}")  #str
print(f"{Eva!r}") #repr