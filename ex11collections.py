# ex11: Collections. Python

import numpy as np

# Same type: numpy's ndarray
foo = np.array([1, 2, 3])
bar = np.array([97, 98, 99])
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

# Immutable: tuple
foo = (1, 'two', 3.33)
bar = foo[2]  # bar=3.33
# foo[2] = 4.44  # ERROR tuples can't change

print(foo, bar, baz)
