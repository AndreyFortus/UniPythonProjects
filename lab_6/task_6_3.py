def create_list():
    with open('C:/Users/Andrii/Desktop/learning_python.txt', 'r', encoding='utf-8') as file:
        return file.readlines()


print(create_list())
