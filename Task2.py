# Multi-paradigm programming languages, Task №2
# Andrey Fortus IKM-221a

GENERAL_INFO = 'Multi-paradigm programming languages, Task №2'
STUDENT_INFO = 'Andrey Fortus IKM-221a'
TEMPLATE = 'Input {} value: '

# info
print(GENERAL_INFO)
print(STUDENT_INFO)

# Math
try:
    x = float(input(TEMPLATE.format('x')))
    y = float(input(TEMPLATE.format('y')))
    z = float(input(TEMPLATE.format('z')))
except ValueError:
    print('Value error! Try again!')
else:
    try:
        result = (pow(12, x) + 17.1) * (y - 254.2) / (17.4 - z) - 4.2
        print(f'Result = {result}')
    except ZeroDivisionError:
        print('Division by zero ! Try another value')
