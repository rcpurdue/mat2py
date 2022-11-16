# ex9: Variables, Python

# Single value
a = 1
b = a;     # Copies value to new variable
b = 99

print(a);   # "1"
print(b);   # "99"

# Values in a container (list)
a = [1, 2 ,3]
b = a     # NOTE Points b at same container as a
b[0] = 99

print(a)   # "[99, 2, 3]"   !!!
print(b)   # "[99, 2, 3]"
