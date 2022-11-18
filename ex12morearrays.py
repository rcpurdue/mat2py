# ex12: More Arrays, MATLAB

import numpy as np

# Commas
foo = np.array([1, 2, 3, 4])  # Commas required

# Autofill
foo = np.zeros(10)
bar = np.ones(20)
baz = np.arange(5)

# Multidimensional
foo = np.array([[1, 2, 3], [4, 5, 6]])  # list of lists
bar = foo.shape
baz = foo.ndim

# Concatenation
foo = np.hstack([[1, 2], [3, 4]])  # --> [1, 2, 3, 4]
bar = np.vstack([[1, 2], [3, 4]])  # 2x2

print(foo, bar, baz)
