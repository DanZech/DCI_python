'''
Your task is to write a program which asks the user about number of arguments in range() function.
If number is 1 program asks for another number and then prints digits from range() function with given number.
If number is 2 program asks for two numbers and then prints digits from range() function with given range.
If number is 3 program asks for three numbers and then prints digits from range() function with given range and given step.

Some of your results could look like this:
Enter number of arguments in range() function: 3
Enter starting number: 2
Enter stopping number: 8
Enter step: 2
2
4
6
rage(start, stop, step)
'''
print('INSTRUCTIONS:\nDigit 1 for RANGE() function just with the start value:\nDigit 2 for START and STOP in a RANGE funcion:\nDigit 3 for START, STOP and STEP in a RANGE funcion: ')
x = int(input('Number:'))
if x == 1:
    start = int(input('Enter number of arguments in RANGE() function: ')) 
    for n in range(start):
        print(start)
if x == 2:
    start = int(input('digit a number to be the START in the RANGE function:')) 
    stop = int(input('digit another number to be the STOP in RANGE function:')) 
    for n in range(start, stop):
        print(n)
if x == 3:
    start = int(input('digit a number to be the START in the RANGE function:')) 
    stop = int(input('digit another number to be the STOP in RANGE function:')) 
    step = int(input('digit another number to be the STEP in RANGE function:')) 
    for n in range(start, stop, step):
        print(n)
    