# Task 2 - get the difference
'''Your task is to write a Python program to get the difference between a two given numbers (prompted by user).
If the first number is greater than second then calculate double difference between numbers.
Otherwise calculate the absolute difference between numbers.
Print out an appropriate message to the user.'''

x = int(input('Digit a integer number: '))
y = int(input('Digit a second integer number: '))

if x > y:
    resul = (x-y)*2
else:
    resul = y - x

print(resul)
