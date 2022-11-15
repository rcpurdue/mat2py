# ex5: Loops, Python

import numpy as np

a = np.array([252, 253, 254])
b = np.array([105, 106, 107])
c = np.gcd(a, b)

for i in range(len(c)):

    if c[i] == 21:
        print('Twenty-one!')
