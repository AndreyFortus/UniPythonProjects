total_sum = 0
with open('C:/Users/Andrii/Desktop/numbers.txt', 'r', encoding='utf-8') as inp,\
     open('C:/Users/Andrii/Desktop/sum_numbers.txt', 'w', encoding='utf-8') as outp:
    for line in inp:
        try:
            num = float(line)
            total_sum += num

        except ValueError:
            print('{} is not a number!'.format(line))
    outp.write(format(total_sum))
    print('Total of all numbers: {}'.format(total_sum))
