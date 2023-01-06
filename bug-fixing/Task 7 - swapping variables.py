a = input("First value: ")
b = input("Second value: ")

print(f"Before swapping: a = {a} b = {b}")

temp_a = a
temp_b = b
b = a
a = temp_b

print(f"After swapping:  a = {a} b = {b}")