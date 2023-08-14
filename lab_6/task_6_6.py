import lab_6.constants


def count_word(file, word):
    return f'\'The\' in {file} = {file.read().lower().count(word)}'


if __name__ == '__main__':
    with open(lab_6.constants.PATH + 'book1.txt', 'r', encoding='utf-8') as book1,\
         open(lab_6.constants.PATH + 'book2.txt', 'r', encoding='utf-8') as book2:
        print(count_word(book1, 'the'))
        print(count_word(book2, 'the'))
