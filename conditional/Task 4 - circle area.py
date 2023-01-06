# Task 4 - circle area
''' Your task is to write a Python program which accepts (prompts) the float radius of a circle 
from the user and compute its area. Round the result to two decimals!
Print out an appropriate message to the user.
Some of your results could look like this:
Input the radius of the circle : 3.45
The area of the circle with radius  3.45  is:  37.39
'''
import math
r = float(input('Input the radius of the circle: '))
a  = (math.pi * r**2)
print(f'The area of the circle with radius {r} is: {round(a,2)}')

