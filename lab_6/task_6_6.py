import io


def count_word(file, word):
    return f'\'The\' in {file} = {file.read().lower().count(word)}'


def count():
    with io.open('C:/Users/Andrii/Desktop/book1.txt', 'r', encoding='utf-8') as book1,\
            open('C:/Users/Andrii/Desktop/book2.txt', 'r', encoding='utf-8') as book2:
        print(count_word(book1, "the"))
        print(count_word(book2, "the"))


count()
