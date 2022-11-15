# ea4: Indexing, Python

import numpy as np

a = np.array([252, 253, 254])
b = np.array([105, 106, 107])

if np.gcd(a, b)[0] == 21:
    print('Twenty-one!')
