# ask for two numbers. If the first one is larger than the second, display the second number first and then the first number.
# otherwise show the first number first and then the second

def two_number(one, two):
    if one > two:
        print('firts number {one}')
    else:
        print("second number {two}")

one = int(input("Enter first number: "))
two = int(input("Enter second number: "))

result = two_number(one, two)
print(result)