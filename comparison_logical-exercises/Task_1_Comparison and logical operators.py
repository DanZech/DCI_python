#task1
print('The software will receive two integer numbers and compare than with each other.')
print('To finish, please, enter "0" (zero) for both inputs')

def equal_test(n1, n2):
    if n1 != n2:
        print('The numbers are different than each other.')
    else:
        print('The numbers are equal.')

def greater(n1, n2):
    if n1 != n2:
        if n1 > n2:
            print('The first number is greater than the second.')
        else:
            print('The second number is greater than the first.')
    else:
        print('We cannot compare equal numbers.')

def even_odd(n1, n2):
    if n1 % 2 == 0:
        print('First number is even.')
    else:
        print('First number is odd')
    if n2 % 2 == 0:
        print('Second number is Even.')
    else:
        print('Second number is ODD')

n1=int(input('Enter the first number:'))
n2=int(input('Enter the second number:'))

while n1 and n2 != 0:
    equal_test(n1, n2)
    greater(n1, n2)
    even_odd(n1, n2)
    n1=int(input('Enter the first number:'))
    n2=int(input('Enter the second number:'))
    
print('Thank you')