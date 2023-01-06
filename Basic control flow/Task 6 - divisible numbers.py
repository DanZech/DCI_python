'''
Task 6 - divisible numbers

Your task is to write a program to print all the numbers between 1000 and 2000 which are divisible by 7 but are not a multiple of 5.

- Some of your results could look like this:

```bash
1001
1008
1022
1029
1036
1043
1057
1064
1071
...
...
1974
1981
1988

'''

number = range(1000, 2001)
lista = []
for n in number:
    if n % 7 == 0:
        if n % 5 != 0:
            lista.append([1])
            print(n)
            lista += [n]
            
print(f'Between 1000 and 2000 we can find {len(lista)} number divisible by 7 but not by 5')