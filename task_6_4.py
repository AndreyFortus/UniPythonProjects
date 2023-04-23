def replace():
    with open('C:/Users/Andrii/Desktop/learning_python.txt', 'r', encoding='utf-8') as t4_str:
        t4_replace = t4_str.read().replace('Python', 'C')
    return t4_replace


print(replace())
