go = (input('Check 3 number for ODD or EVEN: (y or n)'))
while go != 'n':
    x = int(input('First number:'))
    y = int(input('Second number:'))
    z = int(input('Third number:'))
    test = (x, y, z)
    for num in test:
        if num % 2 == 0:
            print(f'{num} is Even.')
        else:
            print(f'{num} is Odd.')
    go = (input('Check 3 number for ODD or EVEN: (y or n)'))