# ex1: Functions, Python

def euclid_gcd(a, b):
    """Return greatest common divisor."""

    while a != b:

        if a > b:
            a = a - b
        else:
            b = b - a

    return a


gcd = euclid_gcd(252, 105)
print(gcd)