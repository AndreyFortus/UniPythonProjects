def calculator():
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x + y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        'mod': lambda x, y: x % y,
        'pow': lambda x, y: x ** y,
        'div': lambda x, y: x // y
    }

    try:
        num_1 = float(input('Input first number: '))
        num_2 = float(input('Input second number: '))
        operation = input('Input math operation: ')
        if operation in ops:
            return f'answer = {ops[operation](num_1, num_2)}'

    except ZeroDivisionError:
        return 'Divided by zero!'
    return 'Error!'


if __name__ == '__main__':
    print(calculator())
