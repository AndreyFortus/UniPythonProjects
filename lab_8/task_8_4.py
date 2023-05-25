def check_num():
    while True:
        try:
            num = int(input())
            return f'{num} is even' if num % 2 == 0 else f'{num} is odd'

        except ValueError:
            return 'Incorrect value. Try again!'


if __name__ == '__main__':
    print(check_num())
