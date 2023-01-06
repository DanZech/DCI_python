'''
Task 5 - FizzBuzz

Your task is to write a program that prints the numbers from 1 to 100.  
 But for multiples of: 
 3 print “Fizz” instead of the number 
 for the  multiples of 5 print “Buzz”.   

 For numbers which are multiples of both three and five print “FizzBuzz”.

- Some of your results could look like this:

```bash
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
'''

number = range(1,101)
for n in number:
    if n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    else:
        print(n)

