# Multi-paradigm programming languages, task №5.1
# Andrey Fortus IKM-221a
from itertools import takewhile, count


# function for finding the sum of a series
def sum_series(n):
    row = (1 / pow(2, n) + 1 / pow(3, n) for n in count())
    print(round(sum(list(takewhile(lambda x: x >= 1e-4, row))), 4))


GENERAL_INFO = 'Multi-paradigm programming languages, task №5.1'
STUDENT_INFO = 'Andrey Fortus IKM-221a variant №20'

# info
print(GENERAL_INFO)
print(STUDENT_INFO)

# finding the sum
n = 1
sum_series(n)
