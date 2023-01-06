#Task 1 - calculate sum
'''Your task is to write a Python program to calculate the sum of three integers given (prompted) by user.
If the values are equal then calculate triple value of their sum.
Print out an appropriate message to the user.'''

x = int(input('Digit a integer number: '))
y = int(input('Digit a second integer number: '))
z = int(input('Digit a last integer number: '))

if x == y == z:
    print((x+y+z)*3)
else:
    print(x+y+z)