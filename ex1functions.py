# ex1: Functions, Python

def euclid_gcd(foo, bar):
    """Return greatest common divisor."""

    while foo != bar:

        if foo > bar:
            foo = foo - bar
        else:
            bar = bar - foo

    return foo


gcd = euclid_gcd(252, 105)
print(gcd)
