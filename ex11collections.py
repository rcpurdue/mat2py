# ex11: Collections. Python

import numpy as np

# Same type: numpy's ndarray
foo = np.array([1, 2, 3])
bar = np.array([97.1, 98.2, 99.3])
baz = foo * bar  # Can do math, note *

# Diff types: list
foo = [1, 'two', 3.33]
bar = ['abc', 'def']  # Can do same type
bar[0] = 'xyz'  # Note same brackets

# Named fields: dictionary
baz = {'shape': 'round',
       'color': 'red',
       'count': 42}
baz['age'] = 99  # New field
baz[4] = 'four'  # Unrestricted field names

# Unchangable: tuple
foo = (1, 'two', 3.33)
bar = foo[2]  # bar=3.33
# foo[2] = 4.44  # ERROR tuples can't change

# Unique: Set
foo = {1, 1, 2, 2, 3, 3}
bar = len(foo)  # bar=3

print(foo, bar, baz)
