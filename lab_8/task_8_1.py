def users(users_list):
    if users_list:
        for user in users_list:
            welcome_text = 'Hello Admin, I hope you\'re well.' if user == 'Admin' else \
                f'Hello {user} thank you for logging in again.'
            print(welcome_text)
    else:
        print('We need to find some users!')


if __name__ == '__main__':
    name_list = ['Alex', 'John', 'Dan', 'Admin', '123_TeSt_321']
    users(name_list)
