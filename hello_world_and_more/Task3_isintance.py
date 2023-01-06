#task3
'''Your task is to check if given value is the instance of given class type using isinstance() function.
The first argument of this function should be value, for example city and the second argument should be class type, for example int.
Print at least one result for every primitive data type ('int', 'float', 'bool', 'complex', and 'str').'''

print()
n1=123 #int
n2=43.23 #float
n3=(10>5) #bool
n4=(3+2j) #complex
n5=("Mandela") #str
print(isinstance(n1, int)) #true
print(isinstance(n2, int)) #false
print(isinstance(n3, bool)) #true
print(isinstance(n4, complex)) #true
print(isinstance(n5, int)) #false