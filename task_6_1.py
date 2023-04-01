total = 0
with open('C:/Users/Andrii/Desktop/numbers.txt', 'r') as inp, open('C:/Users/Andrii/Desktop/sum_numbers.txt', 'w') as outp:
    for line in inp:
        try:
            num = float(line)
            total += num

        except ValueError:
            print('{} is not a number!'.format(line))
    outp.write(format(total))
    print('Total of all numbers: {}'.format(total))
