import re

from constants import PATH


def replace_date(match):
    date = match.group()
    parts = re.split('[./]', date)

    if len(parts[0]) == 4:
        return parts[2] + '.' + parts[1] + '.' + parts[0]
    return parts[0].zfill(2) + '.' + parts[1].zfill(2) + '.' + parts[2].zfill(4)


def main():
    with open(PATH + 'date.txt', 'r', encoding='utf-8') as file_date:
        text = file_date.read()

    pattern = r'\b((0?[1-9]|[12]\d|3[01])[./](0?[1-9]|1[012])[./](\d{4}))' \
              r'|((\d{4})[./](0?[1-9]|1[012])[./](0?[1-9]|[12]\d|3[01]))\b'

    new_text = re.sub(pattern, replace_date, text)

    with open(PATH + 'sorted_date.txt', 'w', encoding='utf-8') as file_sort:
        file_sort.write(new_text)


if __name__ == '__main__':
    main()
