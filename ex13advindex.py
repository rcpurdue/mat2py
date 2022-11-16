# ex13: Advanced Indexing, MATLAB

import numpy as np

foo = np.array([11, 22, 33, 44])

# Iterating over all values
for i in range(len(foo)):   # len(foo)=4, range(4)=0, 1, 2, 3
    print(foo[i])

# Slicing
bar = foo[1:2];  # bar=[22, 33]

# Slicing to the last item
baz = foo[1:];  # baz=[22, 33, 44]

# Changing a value in a slice
baz[0] = 0;  # NOTE foo=[0, 22. 33, 44], baz=[0, 33, 44]  !!!

# Get the last value: NOTE "Negative means wrap around from 0"
bar = foo[-1];  # bar=44

# Backwards indexing
bar = foo(-2);  # len(foo)=4, 4-2=2, bar="22"
