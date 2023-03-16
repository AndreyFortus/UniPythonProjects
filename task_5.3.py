# Multi-paradigm programming languages, task №5.3
# Andrey Fortus IKM-221a
import math

GENERAL_INFO = 'Multi-paradigm programming languages, task №5.3'
STUDENT_INFO = 'Andrey Fortus IKM-221a variant №20'

# info
print(GENERAL_INFO)
print(STUDENT_INFO)


# Square root function
def square_root(a):
    x = a
    while abs(x * x - a) > 1e-8:
        x = (x + a / x) / 2
    return round(x, 3)


n = float(input('Input value: '))
print(f'Square {n} equal {square_root(n)}') if n >= 0 else print('Value must be greater than 0')
