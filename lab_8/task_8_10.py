def chess():
    coord = input('Input figure coordinates (example: d4): ')
    if 96 < ord(coord[0]) < 105 and 48 < ord(coord[1]) < 57:
        color = 'black' if (ord(coord[0]) + ord(coord[1])) % 2 == 0 else 'white'
        return f'square is {color}'
    return 'Out of chess field'


if __name__ == '__main__':
    print(chess())
