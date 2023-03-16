# Multi-paradigm programming languages, task №5.1
# Andrey Fortus IKM-221a

GENERAL_INFO = 'Multi-paradigm programming languages, task №5.1'
STUDENT_INFO = 'Andrey Fortus IKM-221a variant №20'

# info
print(GENERAL_INFO)
print(STUDENT_INFO)


# function for finding the sum of a series
def sum_series(n):
    suma = 1  # start value
    while 1 / pow(2, n) + 1 / pow(3, n) >= 1e-4:  # 1e-4 = 1 * 10−4
        suma += 1 / pow(2, n) + 1 / pow(3, n)
        n += 1
    return round(suma, 4)


n = 1
sum_series(n)
print(f'Sum of the series with precision e = 10^-4: {sum_series(n)}')
