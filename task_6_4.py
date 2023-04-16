with open('C:/Users/Andrii/Desktop/learning_python.txt', 'r', encoding='utf-8') as t4_str:
    for line in t4_str:
        t4_replace = line.replace('Python', 'C')

print(t4_replace)
