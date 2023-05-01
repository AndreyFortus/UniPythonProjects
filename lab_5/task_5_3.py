# Multi-paradigm programming languages, task №5.3
# Andrey Fortus IKM-221a

# Square root function
def square_root(a):
    xi = a
    while abs(xi * xi - a) > 1e-8:
        xi = (xi + a / xi) / 2
    return round(xi, 3)


GENERAL_INFO = 'Multi-paradigm programming languages, task №5.3'
STUDENT_INFO = 'Andrey Fortus IKM-221a variant №20'

# info
print(GENERAL_INFO)
print(STUDENT_INFO)


# find square root
try:
    n = float(input('Input value: '))
except ValueError:
    print('Value must not be string!')
else:
    if n < 0:
        raise Exception('value must be equal or greater than 0')
    print(f'Square {n} equal {square_root(n)}')
