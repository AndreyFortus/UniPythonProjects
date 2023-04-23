def create_list():
    list_str = []
    with open('C:/Users/Andrii/Desktop/learning_python.txt', 'r', encoding='utf-8') as lstr:
        for __ in lstr:
            list_str.append(lstr.readlines())

    return list_str


print(create_list())
