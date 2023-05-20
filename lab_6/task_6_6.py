import const_file


def count_word(file, word):
    return f'\'The\' in {file} = {file.read().lower().count(word)}'


def main():
    with open(const_file.PATH + 'book1.txt', 'r', encoding='utf-8') as book1,\
         open(const_file.PATH + 'book2.txt', 'r', encoding='utf-8') as book2:
        print(count_word(book1, "the"))
        print(count_word(book2, "the"))


main()
