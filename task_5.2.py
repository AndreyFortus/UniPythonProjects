# Multi-paradigm programming languages, task №5.2
# Andrey Fortus IKM-221a

GENERAL_INFO = 'Multi-paradigm programming languages, task №5.2'
STUDENT_INFO = 'Andrey Fortus IKM-221a variant №20'

# info
print(GENERAL_INFO)
print(STUDENT_INFO)


# digits counter
def digits_counter(n):
    counter = 1
    while abs(n) >= 10:
        n = n / 10
        counter += 1
    return counter


n = int(input('Input n value: '))
print(f'Digits in n = {digits_counter(n)}')
