list_str = []
with open('C:/Users/Andrii/Desktop/learning_python.txt', 'r') as lstr:
    for line in lstr:
        line = line.strip()
        list_str.append(lstr.readlines())

print(list_str)
