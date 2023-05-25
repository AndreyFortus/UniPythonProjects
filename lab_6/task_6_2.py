import constants
from utils import int_checker


def number_check():
    number = int_checker()
    with open(constants.PATH + 'task_6_2.txt', 'w', encoding='utf-8') as file:
        file.write(f"number {number} is {'even' if number % 2 == 0 else 'odd'}")


if __name__ == '__main__':
    number_check()
