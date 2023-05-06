def replace_word():
    with open('C:/Users/Andrii/Desktop/learning_python.txt', 'r', encoding='utf-8') as t4_str:
        t4_replace = t4_str.read().replace('Python', 'C')
    print(t4_replace)


replace_word()
