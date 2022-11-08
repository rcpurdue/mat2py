# euclidean_algorithm.py, rcampbel@purdue.edu
# Ref: https://en.wikipedia.org/wiki/Euclidean_algorithm

a = 252
b = 105

while a != b:

    if a > b:
        a = a - b
    else:
        b = b - a

print(a)
