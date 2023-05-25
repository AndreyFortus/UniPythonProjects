import constants


def replace_word():
    with open(constants.PATH + 'learning_python.txt', 'r', encoding='utf-8') as t4_str:
        print(t4_str.read().replace('Python', 'C'))


if __name__ == '__main__':
    replace_word()
