# ex14: Expanding Arrays, Python

import numpy as np

foo = np.array([1, 2, 3]);

# Append values
foo = np.append(foo, 4)  # foo=[1, 2. 3, 4]

# Automatic expansion - not allowed
# foo[11] = 99;  # ERROR index out of bounds!

# Manual expansion
foo = np.hstack([foo, np.zeros(8)])
foo[11] = 99  # foo=[1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 99]
