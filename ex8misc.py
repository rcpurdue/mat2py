# ex8: Misc., MATLAB

import math

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
    foo, bar = math.frexp(3.14)
    foo = math.frexp(3.14)
    _, foo = math.frexp(3.14)

except Exception as e:

    # Formatted output
    print(f'Error: {e}')
