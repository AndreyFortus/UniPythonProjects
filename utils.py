def int_checker():
    try:
        return int(input('input your number: '))
    except ValueError:
        return 'Your input is incorrect! Must be integer value.'