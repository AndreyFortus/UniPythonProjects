def users(users_list):
    welcome_list = []
    if users_list:
        for user in users_list:
            welcome_list.append('Hello Admin, I hope you\'re well.' if user == 'Admin' else
                                f'Hello {user} thank you for logging in again.')
        return welcome_list
    return 'We need to find some users!'


if __name__ == '__main__':
    name_list = ['Alex', 'John', 'Dan', 'Admin', '123_TeSt_321']
    print(users(name_list))
