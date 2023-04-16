import io

with io.open('C:/Users/Andrii/Desktop/book1.txt', 'r', encoding='utf-8') as book1,\
        open('C:/Users/Andrii/Desktop/book2.txt', 'r', encoding='utf-8') as book2:
    count1 = book1.read().lower().count("the")
    count2 = book2.read().lower().count("the")
    print(f'\'The\' in book №1 = {count1}')
    print(f'\'The\' in book №2 = {count2}')
