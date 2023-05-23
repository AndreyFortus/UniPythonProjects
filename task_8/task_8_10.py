def chess():
    coord = input('Input figure coordinates (example: d4): ')
    # if 104 < ord(coord[0]) < 57 \
    #         or 57 < ord(coord[1]) < 49:
    if 104 < ord(coord[0]) or ord(coord[0]) < 57 \
            or 57 < ord(coord[1]) or ord(coord[1]) < 49:
        return 'Out of chess field'
    color = 'black' if (ord(coord[0]) + ord(coord[1])) % 2 == 0 else 'white'
    return f'square is {color}'


if __name__ == '__main__':
    print(chess())
