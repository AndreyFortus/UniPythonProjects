def replace_symbol():
    with open('C:/Users/Andrii/Desktop/book1.txt', 'r', encoding='utf-8') as book,\
         open('C:/Users/Andrii/Desktop/formatted_text.txt', 'w', encoding='utf-8') as fbook:
        fbook.write(book.read().replace(' ', '_'))


replace_symbol()
