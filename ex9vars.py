# ex9: Variables, Python

# Single value
foo = 1
bar = foo;     # Copies value to new variable
bar = 99

print(foo);   # "1"
print(bar);   # "99"

# Values in a container (list)
foo = [1, 2 ,3]
bar = foo     # NOTE Points b at same container as a
bar[0] = 99

print(foo)   # "[99, 2, 3]"   !!!
print(bar)   # "[99, 2, 3]"
