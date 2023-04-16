import io

with io.open('C:/Users/Andrii/Desktop/book1.txt', 'r', encoding='utf-8') as book,\
        open('C:/Users/Andrii/Desktop/formatted_text.txt', 'w', encoding='utf-8') as fbook:
    text = book.read()
    formatted_text = text.replace(' ', '_')
    fbook.write(formatted_text)
