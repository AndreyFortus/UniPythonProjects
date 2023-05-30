def money():
    money_dict = {
        1: 'Volodimir The Great',
        2: 'Yaroslav the Wise',
        5: 'Bohdan Khmelnytsky',
        10: 'Ivan Mazepa',
        20: 'Ivan Franko',
        50: 'Mykhailo Hrushevskyi',
        100: 'Taras Shevchenko',
        200: 'Lesia Ukrainka',
        500: 'Hryhorii Skovoroda',
        1000: 'Volodymyr Vernadskyi'
    }

    nominal = int(input('Input nominal: '))
    if nominal in money_dict:
        return f'{money_dict[nominal]} is depicted on {nominal} hryvnias'
    return 'Nominal not found. Try another'


if __name__ == '__main__':
    print(money())
