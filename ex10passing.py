# ex10: Passing, Python

def change(b):
    b[0] = 99

a = [1, 2, 3]
change(a)
print(a)   # "[99, 2, 3]"   !!!
