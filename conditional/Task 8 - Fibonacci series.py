# Task 8 - Fibonacci series
'''Your task is to write a Python program to get the Fibonacci series between 0 to 50.

Note: The Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.'''

n1 =  0 #int(input('Enter the fisrt number: '))
n2 = 1 #int(input('Enter the second number: '))
#lenght= 7 #int(input('Enter many number in the Fibonacci sequence: '))

print(n1) 
print(n2)
x = 3
while x <= 50:   
    n_var = n1 + n2
    print(n_var)
    n1 = n2
    n2 = n_var
    n_var = n1 + n2 
    x = x + 1 
