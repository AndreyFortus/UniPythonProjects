import lab_6.constants


def replace_symbol():
    with open(lab_6.constants.PATH + 'book1.txt', 'r', encoding='utf-8') as book,\
         open(lab_6.constants.PATH + 'formatted_text.txt', 'w', encoding='utf-8') as fbook:
        fbook.write(book.read().replace(' ', '_'))


if __name__ == '__main__':
    replace_symbol()
