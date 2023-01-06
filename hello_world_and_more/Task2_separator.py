#task2
'''Your task is to print two objects with separator for the same primitive types as in task 1.
The first object is a value of given type, the second object is a type of value.
The separator is a string " is type of ".'''
a1=234
a2=43.12
a3=(3+2j)
a4='Hello'
a5=10>5
print(a1, a2, a3, a4, a5, sep="\n")
print()
print(f'{a1} is type of {type(a1)}')
print(f'{a2} is type of {type(a2)}')
print(f'{a3} is type of {type(a3)}')
print(f'{a4} is type of {type(a4)}')
print(f'{a5} is type of {type(a5)}')