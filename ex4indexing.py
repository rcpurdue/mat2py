# ea4: Indexing, Python

import numpy as np

foo = np.array([252, 253, 254])
bar = np.array([105, 106, 107])

if np.gcd(foo, bar)[0] == 21:
    print('Twenty-one!')
