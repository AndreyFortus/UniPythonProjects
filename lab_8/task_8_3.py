import numpy as np


def check_numbers(number):
    if number == 1:
        return f'{number}st'
    if number == 2:
        return f'{number}nd'
    if number == 3:
        return f'{number}rd'
    return f'{number}th'


def numbers(list_num):
    list_num_with_ends = [check_numbers(number) for number in list_num]
    return list_num_with_ends


def main():
    list_numbers = np.arange(1, 10, 1)
    print(numbers(list_numbers))


if __name__ == '__main__':
    main()
