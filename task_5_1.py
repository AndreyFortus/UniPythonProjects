# Multi-paradigm programming languages, task №5.1
# Andrey Fortus IKM-221a
from itertools import takewhile, count


# function for finding the sum of a series
def sum_series(ni):
    row = (1 / pow(2, ni) + 1 / pow(3, ni) for ni in count())
    ni = round(sum(list(takewhile(lambda x: x >= 1e-4, row))), 4)
    return ni


GENERAL_INFO = 'Multi-paradigm programming languages, task №5.1'
STUDENT_INFO = 'Andrey Fortus IKM-221a variant №20'

# info
print(GENERAL_INFO)
print(STUDENT_INFO)

# finding the sum
n = 1
print(sum_series(n))
