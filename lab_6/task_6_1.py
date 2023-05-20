import const_file


def total_count(total):
    with open(const_file.PATH + 'numbers.txt', 'r', encoding='utf-8') as inp, \
            open(const_file.PATH + 'sum_numbers.txt', 'w', encoding='utf-8') as outp:
        for line in inp:
            try:
                total += float(line)
            except ValueError:
                print(f'{line} not a number!')
        outp.write(total)
        return f'Total of all numbers: {total}'


def main():
    print(total_count(0))


main()
