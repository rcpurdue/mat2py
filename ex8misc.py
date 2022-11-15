# ex8: Misc., MATLAB

a = True    # Boolean value
b = None    # Empty value
c = 'abc'   # String

try:

    # Expressions
    if a or (b is None and c == 'abc'):
        print('Ok')
    else:
        print('Nope')

except Exception as e:

    # Formatted output
    print(f'Error: {e}')
