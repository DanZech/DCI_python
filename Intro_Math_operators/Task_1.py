'''
Task 1 - basic math operations

Your task is to check in action every basic math operators with combination of integers, floating point numbers, complex numbers and booleans. 
Do at least two calculations for every operator. 

Also make use of [round()](https://www.w3schools.com/python/ref_func_round.asp) function to round your floating point results to specific number of decimals.  

You can mix integer with floats inside given math operation.  
Hint: You can assign math operation to a variable, and then perform another math operation on this variable, for example:  
'''

import math
n1 = float(input('Enter the first number:'))
n2 = float(input('Enter the second number:'))
n3 = float(input('Enter a float numbr with some decimal digits: '))

print(f'Sum of {n1} and {n2} is {n1 + n2}')
print(f'Substraction of {n1} and {n2} is {n1 - n2}')
print(f'{n1} multiplied by {n2} is {n1 * n2}')
print(f'{n1} divided {n2} is {n1 / n2}')
print(f'Modulo (%) of {n1} and {n2} is {n1 % n2}')
print(f'{n1} powered by {n2} is {n1 ** n2}')
print()
print(f'Making your float numeber round up we have {math.ceil(n3)} and round down {math.floor(n3)}.')

