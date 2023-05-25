

def figure(sides):
    list_figures = ['triangle', 'square', 'pentagon', 'hexagon']
    if 6 > sides or sides > 3:
        for i, _ in enumerate(list_figures):
            if sides == i + 3:
                return f'The figure with {sides} sides is {list_figures[i]}'
    return 'for the correct operation of the program, the number of sides must be 3-6'


if __name__ == '__main__':
    print(figure(3))
