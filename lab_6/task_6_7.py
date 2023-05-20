import const_file


def replace_symbol():
    with open(const_file.PATH + 'book1.txt', 'r', encoding='utf-8') as book,\
         open(const_file.PATH + 'formatted_text.txt', 'w', encoding='utf-8') as fbook:
        fbook.write(book.read().replace(' ', '_'))


replace_symbol()
