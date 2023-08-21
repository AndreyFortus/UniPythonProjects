def figure(sides):
    figures_dict = {3: 'triangle', 4: 'square', 5: 'pentagon', 6: 'hexagon'}
    if 6 >= sides >= 3:
        if sides in figures_dict:
            return f'The figure with {sides} sides is {figures_dict[sides]}'
    return 'for the correct operation of the program, the number of sides must be 3-6'


if __name__ == '__main__':
    print(figure(3))
