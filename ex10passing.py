# ex10: Passing, Python

def change(bar):
    bar[0] = 99

foo = [1, 2, 3]
change(foo)
print(foo)   # "[99, 2, 3]"   !!!
