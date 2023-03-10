# Multi-paradigm programming languages, Task №3
# Andrey Fortus IKM-221a
import math

GENERAL_INFO = 'Multi-paradigm programming languages, Task №3'
STUDENT_INFO = 'Andrey Fortus IKM-221a'

# info
print(GENERAL_INFO)
print(STUDENT_INFO)

# Math
x = float(input('Enter x value: '))
z = float(input('Enter z value: '))
try:
    y = z + x / (pow(z, 2) - math.fabs(pow(x, 2) / (z - pow(x, 3) / 3)))
    print(f'y = {y}')
except ZeroDivisionError:
    print('Division by zero ! Try another value')
