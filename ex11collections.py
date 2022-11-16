# ex11: Collections. Python

import numpy as np

# numpy's "ndarray": holds values of same type
foo1 = np.array([1, 2, 3])
foo2 = np.array([97, 98, 99])
foo3 = foo1 * foo2;  # Can do math - NOTE "*"

# "list": holds values of different types
bar1 = [1, 'two', 3.33]
bar2 = ['abc', 'def']  # Sometimes holds values of same type
bar2[0] - 'xyz'  # NOTE same index operators, "[...]"

# "dictionary": holds values in named fields
baz = {'shape': 'round',
       'color': 'red',
       'count': 42}
baz['color'] = 'green'  #Ok to change value of field
baz['age'] = 99  # Ok to add new fields
baz[4] = 'four'  # OK to use any value as a field name

# "tuple":  also holds values of diff types
foo = (1, 'two', 3.33)
bar = foo[2]  # use square brackets to index, bar=3.33
foo[2] = 4.44  # ERROR tuples cannot change ("immutable")
