# ex8: Misc., MATLAB

foo = True    # Boolean value
bar = None    # Empty value
baz = 'abc'   # String

try:

    # Expressions
    if foo or (bar is None and baz == 'abc'):
        print('Ok')
    else:
        print('Nope')

except Exception as e:

    # Formatted output
    print(f'Error: {e}')
