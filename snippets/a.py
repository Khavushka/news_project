'''
1. Checking if alist Empty:
one common task in Python is checking whether a list is empty. Instead of using a verbose if-else statement, you can use the simplicity of Python to your advantage with the following code snoppet
'''

my_list = [1, 2, 4, 6, 2, 7, 8, 2]
# my_list = []
if not my_list:
    print("The list is empty")
else:
    print("The list is not empty")
    

'''
2. Reversing a String
Python provides an elegant way to reverse a string using slicing. Here's a code snippet that demonstrates this:
'''

my_string = "Hello, World"
reversed_string = my_string[::-1]
print(reversed_string) #the '[::-1]' slicing syntax allows you to reverse the order of the characters in a string effortlessly

'''
3. Calculating the Factorial of a Number:
the factorial of a non-negative integer `n`. The following recursive code snippet calculates the factorial of a number:
'''
def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)
    
result = factorial(5)
print(result)


'''
4. Finding the Most frequent element in a List:
to find the most frequently occuring element in a list, you can leverage the `Counter` class from the `collections` module. Here's an example:
'''
from collections import Counter
# my_list = [1, 2, 3, 4, 2, 6, 3, 8]
most_common_element = Counter(my_list).most_common(1)[0][0]
print(most_common_element)


'''
5. Checking for anagrams:
determining whether two strings are anagrams (i.e., contain the same characters in a different order) can be accomplished by comparing sorted versions of the strings. Here's code snippet:
'''
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

result = is_anagram("Listen", "silent")
print(result)
# this code snippet efficiently checks if two strings are anagrams by sorteing them and comparing the soretd versions


'''
6. Removing Duplicates from a List:
to remove duplicates from a list while preserving the order of the elements, you can use a combination of list comprehension and the set() funstion:
'''
# my_list = [1, 2, 4, 2, 6, 2]  # Zakomentirovala iz-za togo chto tam uzhe est my_list naverhu
unique_list = list(set(my_list))
print(unique_list)


'''
7. Checking if a string contains a substring:
to check if a string contains a specific substring, you can use the in keyword:
'''
# my_string = "Hello, World!" #Zakomentirovano iz-za togo, chto my_string uzhe nahoditsya naverhu
if "World" in my_string:
    print("Substring found!")
else:
    print("Substring not found!") 
    
    
'''
8.Converting a string to Title Case:
to convert a string to tilte case (where the first letter of each word is capitalized), you can use the title() method:
'''
# my_string = "Hello, World!" #Zakomentirovano iz-togo chto uzhe est naverhu my_string
# title_case_string = my_string.title() 
# title_case_string = my_string.capitalize() 
# title_case_string = my_string.upper() 
title_case_string = my_string.lower() 
print(title_case_string)