x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x == y or y == z:
    result = 0
else:
    result = x + y + z
print("Calculated sum is ", result)