# ex5: Loops, Python

import numpy as np

foo = np.array([252, 253, 254])
bar = np.array([105, 106, 107])
baz = np.gcd(foo, bar)

for i in range(len(baz)):  # range(3) --> 0, 1, 2

    if baz[i] == 21:
        print('Twenty-one!')
