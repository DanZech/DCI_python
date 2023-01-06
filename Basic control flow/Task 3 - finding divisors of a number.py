'''
Task 3 - finding divisors of a number

Your task is to write a program which prints all the divisors of a number. 
The number comes from the user's input.

- Some of your results could look like this:

```bash
Enter number: 56
2
4
7
8
14
28
56
'''


num = int(input('Digit a number and we will find out all the divisors:'))

for n in range(1, num):
    x = num % n
    if x == 0:
        print(n)
print(num)   