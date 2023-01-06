months30 = [4 , 6, 9, 11]
months28 = 2
months31 = [1, 3, 5, 7, 10, 12]
month = -1

def checkForInput():
    userInput = input('Digit a month number or 0 to quit: ')
    if userInput.isnumeric():
        return int(userInput)
    else:
        return -1

print('Please, digit a valid number (1 till 12), or 0 to quit:')

while month != 0:
    month = checkForInput()
    if month in months30:
        print(30)
    elif month in months31:
        print(31)
    elif month == 2:
        year_bi = input('Is it a leap year (y or n): ')
        if year_bi == 'y':
            print(29)
        else:
            print(28)
    elif month == 0:
        print("Program end")
    else:
        print("Not a valid input")

