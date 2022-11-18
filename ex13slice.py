# ex13: Slicing, MATLAB

import numpy as np

foo = np.array([11, 22, 33, 44])

# Slicing creates "view" into orig
bar = foo[1:2]  # bar=[22, 33]
bar[0] = 0  # foo=[0, 22. 33, 44], bar=[0, 33, 44]  !!!

baz = foo[1:]  # Slice to end
baz = foo[-1]  # Last value: "negative means wrap around"
baz = foo[-2]  # Backwards indexing

print(foo, bar, baz)

foo = np.array([[1, 2, 3], [4, 5, 6]])

# Colon alone, "all"
bar = foo[:, 1]  # [2, 5]
bar = foo[0, :]  # [1, 2, 3]
bar = foo[:]  # 2x3: [[1, 2, 3], [4, 5, 6]]  !!!

# Partial indexes
baz = foo[0]  # [1, 2, 3] !!!

print(foo, bar, baz)
