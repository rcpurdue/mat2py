# ex8: Misc., MATLAB

import numpy as np

foo = True    # Boolean value
bar = None    # Empty value
baz = 'abc'   # String

# Exception handling
try:

    # Expressions
    if foo or (bar is None and baz == 'abc'):
        print('Yep')
    else:
        print('Nope')

    # Multiple return values
    foo, bar = np.meshgrid([1, 2], [1, 2, 3])
    foo = np.meshgrid([1, 2], [1, 2, 3])  # only 1st
    _, foo = np.meshgrid([1, 2], [1, 2, 3])  # only 2nd

except Exception as e:

    # Formatted output
    print(f'Error: {e}')
