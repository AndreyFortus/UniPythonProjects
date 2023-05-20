import const_file


def create_list():
    with open(const_file.PATH + 'learning_python.txt', 'r', encoding='utf-8') as file:
        return file.readlines()


print(create_list())
