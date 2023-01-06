#  Task 6 - Celsius to Fahrenheit conversion
''' Your task is to write a Python program to convert temperatures to and from Celsius, Fahrenheit.

In the centigrade scale, which is also called the Celsius scale, water freezes at 0 degrees and boils at 100 degrees.
In the Fahrenheit scale, water freezes at 32 degrees and boils at 212 degrees.

Note : User should be prompted twice:

to enter a temperature,
to enter a shortcut for given scale (C for Celsius, F for Fahrenheit).
Formula : C/5 = F-32/9, where C = temperature in Celsius and F = temperature in Fahrenheit.

Some of your results could look like this:

Input the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius: C
Input the value of temperature you'd like to convert  : 60
The temperature in Fahrenheit is 140 degrees.'''


print('Please, choose below what you want to convert:\n1 - Fahenreit to Celsius\n2 - Celsius to Farenheit')
measure = int(input('>'))
if measure == 1:
    f = float(input('Enter the temperature in Farenheit:'))
    c = ((f-32)/9)*5
    print(c)
elif measure == 2:
    c = float(input('Enter the temperature in Celsius:'))
    f = (c * 1.8 + 32)
    print(f)
else:
    print('Invalid input!')