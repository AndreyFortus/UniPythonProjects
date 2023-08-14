import lab_6.constants


def replace_word():
    with open(lab_6.constants.PATH + 'learning_python.txt', 'r', encoding='utf-8') as t4_str:
        return t4_str.read().replace('Python', 'C')


if __name__ == '__main__':
    print(replace_word())
