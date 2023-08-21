from lab_8.task_8_6 import year_check


def month_check():
    month_dict = {
        'january': 31, 'march': 31, 'may': 31, 'july': 31, 'august': 31, 'october': 31,
        'december': 31,

        'april': 30, 'june': 30, 'september': 30, 'november': 30
    }
    while True:
        month = input('Input month for more info: ').lower()
        if month in month_dict:
            return f'in {month} {month_dict[month]} days'
        if month.lower() == 'february':
            year = int(input('Input year: '))
            return f'in {month} 28 days' if year_check(year) == 'Ordinary year' \
                else f'in {month} 29 days'


if __name__ == '__main__':
    print(month_check())
