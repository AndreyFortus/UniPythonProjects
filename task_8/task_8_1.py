def users(users_list):
    if not users_list:
        print('We need to find some users!')
    else:
        for user in users_list:
            welcome_text = 'Hello Admin, I hope you\'re well.' if user == 'Admin' else \
                f'Hello {user} thank you for logging in again.'
            print(welcome_text)


if __name__ == '__main__':
    name_list = ['Alex', 'John', 'Dan', 'Admin', '123_TeSt_321']
    users(name_list)
