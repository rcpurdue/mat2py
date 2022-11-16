# ex12: Advanced Arrays, MATLAB

import numpy as np

# Commas
bar = np.array([1, 2, 3, 4])  # NOTE commas required

# Autofill
foo = np.zeros(10);  # [0, 0, 0, 0, 0, 0, 0, ...]
bar = np.ones(20);  # [1, 1, 1, 1, 1, 1, 1, ...]
baz = np.arange(5);  # [0, 1, 2, 3, 4]  NOTE five values

# Multidimensional
foo = np.array([[1, 2, 3], [4, 5, 6]]);  # NOTE lists
bar = foo.shape;  # get value of attribute "shape", bar=(2, 3])
baz = foo.ndim;  # get value of attribute "ndim", baz=2

# Concatenation
foo = np.concatenate([[1, 2], [3, 4]]);  # foo=[1, 2, 3, 4]
bar = np.hstack([[1, 2], [3, 4]]);  # Same as above
baz = np.vstack([[1, 2], [3, 4]]);  # Creates 2x2
