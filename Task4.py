# Multi-paradigm programming languages, Task №4
# Andrey Fortus IKM-221a

GENERAL_INFO = 'Multi-paradigm programming languages, Task №4'
STUDENT_INFO = 'Andrey Fortus IKM-221a'

# info
print(GENERAL_INFO)
print(STUDENT_INFO)


# function for Fibonacci numbers
def fibonacci(n):
    if n < 0:
        print("n must be more then 0!")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# print n is the number of Fibonacci numbers
n = int(input('Input number of Fibonacci numbers: '))
print('Fibonacci numbers: ')
for i in range(n):
    print(f'{fibonacci(i)}, ', end='')
