def int_checker():
    try:
        return int(input('Input your number: '))
    except ValueError:
        return 'Your input is incorrect! Must be integer value.'
