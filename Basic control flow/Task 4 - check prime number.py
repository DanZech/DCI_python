'''
Task 4 - check prime number

Your task is to write a program to check if input number is a prime number.  
>Hint: Prime number divides without rest only by 1 and itself!

- Some of your results could look like this:

```bash
Enter number: 63
63  is not a prime number
```
'''
n = int(input("Digit a number: "))
mult=0
for count in range(2,n):
    if (n % count == 0):
        mult += 1
        
if mult==0:
    print(f'{n} is a PRIME number.')
if mult >= 1:
    print(f'{n} is not a PRIME number.')