list_str = []
with open('C:/Users/Andrii/Desktop/learning_python.txt', 'r', encoding='utf-8') as lstr:
    for line in lstr:
        line = line.strip()
        list_str.append(lstr.readlines())

print(list_str)
