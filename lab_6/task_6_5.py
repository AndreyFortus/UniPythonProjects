import const_file


def user_list():
    with open(const_file.PATH + 'guest_book.txt', 'w', encoding='utf-8') as guest_b:
        username = None
        while username != 'exit':
            username = input('(Input \'exit\' to stop program) Input your name:')
            welcome_user = f'Welcome {username}!\n'
            print(welcome_user)
            guest_b.write(welcome_user)

        print('Thx for use our program!')


user_list()
