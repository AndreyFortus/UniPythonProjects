# Multi-paradigm programming languages, Task №4
# Andrey Fortus IKM-221a

GENERAL_INFO = 'Multi-paradigm programming languages, Task №4'
STUDENT_INFO = 'Andrey Fortus IKM-221a'

# info
print(GENERAL_INFO)
print(STUDENT_INFO)


# function for Fibonacci numbers
def fibonacci(n):
    if n == 0:
        return 0
    elif n < 3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# print n is the number of Fibonacci numbers
try:
    n = int(input('Input number of Fibonacci numbers: '))
except ValueError:
    print('Invalid value! Try again!')
else:
    if n <= 0:
        print('number must be more then 0!')
    elif n > 0:
        print('Fibonacci numbers: ')
        fib_list = [fibonacci(i) for i in range(n)]
        print(fib_list)
