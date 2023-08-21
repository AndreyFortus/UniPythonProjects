def binary_convert(num_dec):
    result = ''
    while num_dec:
        result += f'{num_dec % 2}'
        num_dec //= 2
    return result[::-1]


def decimal_convert(num_bin):
    decimal, i = 0, 0
    while num_bin:
        decimal = decimal + num_bin % 10 * pow(2, i)
        num_bin //= 10
        i += 1
    result = decimal
    return result


if __name__ == '__main__':
    print(binary_convert(2019))
    print(decimal_convert(11111100011))
