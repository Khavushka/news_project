'''
create the following using a simple 2d list using the standard python indexing.
'''
# grades = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
# print(grades)


'''
after gathering the four names, ages and shoe sizes, ask the user to enter the name of the person they want to remove from the list. delete this row from the data and display the other rows on separate lines
'''
four_names = [{'Susan':{'Ma': 45, "En": 37, "Fr": 54},"Peter":{"Ma":62,"En": 46,"Fr":23}}]
# print(four_names)
user = input("Enter name you want to remove from the list: ")
if user in four_names:
    del four_names[user]
    print(user)
print(four_names)