import constants


def replace_symbol():
    with open(constants.PATH + 'book1.txt', 'r', encoding='utf-8') as book,\
         open(constants.PATH + 'formatted_text.txt', 'w', encoding='utf-8') as fbook:
        fbook.write(book.read().replace(' ', '_'))


if __name__ == '__main__':
    replace_symbol()
