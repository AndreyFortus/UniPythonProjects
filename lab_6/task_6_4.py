import const_file


def replace_word():
    with open(const_file.PATH + 'learning_python.txt', 'r', encoding='utf-8') as t4_str:
        print(t4_str.read().replace('Python', 'C'))


replace_word()
