import lab_6.constants


def total_count():
    total = 0
    with open(lab_6.constants.PATH + 'numbers.txt', 'r', encoding='utf-8') as inp, \
            open(lab_6.constants.PATH + 'sum_numbers.txt', 'w', encoding='utf-8') as outp:

        for line in inp:
            try:
                total += float(line)
            except ValueError:
                print(f'{line} not a number!')
        outp.write(format(total))
        return f'Total of all numbers: {total}'


if __name__ == '__main__':
    print(total_count())
