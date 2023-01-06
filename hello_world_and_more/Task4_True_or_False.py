#task4
'''Your task is a slightly modification of task 3. 
Instead printing True or False modify your code to get readable information about the type of your value.'''

print()
n1=123 #int
n2=43.23 #float
n3=(10>5) #bool
n4=(3+2j) #complex
#n5=("Mandela") #str
n6=('"How are you?"') #str
print(f'Is {n1} an instance of int? {isinstance(n1 , int)}') #true
print(f'Is {n2} an instance of bool? {isinstance(n2, int)}') #false
print(f'Is {n4} an instance of complex? {isinstance(n4, complex)}') #true
print(f'Is {n3} an instance of bool? {isinstance(n3, bool)}') #true
print(f'Is {n6} an instance of float? {isinstance(n6, int)}') #false
print()

print('task 5: comment done for task 4. Please, check the code.')
print()