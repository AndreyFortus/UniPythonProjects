TOTAL = 0
with open('C:/Users/Andrii/Desktop/numbers.txt', 'r', encoding='utf-8') as inp,\
     open('C:/Users/Andrii/Desktop/sum_numbers.txt', 'w', encoding='utf-8') as outp:
    for line in inp:
        try:
            num = float(line)
            TOTAL += num

        except ValueError:
            print(f'{line.format()} not a number!')
    outp.write(format(TOTAL))
    print('Total of all numbers: {}'.format(TOTAL))
