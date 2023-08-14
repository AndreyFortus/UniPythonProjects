import re

from constants import PATH


def find_year():
    with open(PATH + 'text_with_dates.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    pattern = r'\b\d{3,4}\b'
    years_list = [(int(year), i + 1) for year in re.findall(pattern, line) for i, line in enumerate(lines)]

    for year, line_number in years_list:
        print(f'Year: {year}, row: {line_number}')


if __name__ == '__main__':
    find_year()
