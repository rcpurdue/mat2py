# ex9: Variables, Python

# Single value, "immutable"
foo = 1
bar = foo  # Copy value
bar = 99

print(foo, bar)  # 1 99

# Values in container (list),  "mutable"
foo = [1, 2, 3]
bar = foo     # Point b at SAME list
bar[0] = 99

print(foo, bar)   # [99, 2, 3] [99, 2, 3] !!!
