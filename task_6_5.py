with open('C:/Users/Andrii/Desktop/guest_book.txt', 'w', encoding='utf-8') as guest_b:
    while True:
        username = input('(Input \'exit\' to stop program) Input your name:')
        if username == 'exit':
            print('Thx for use our program!')
            break

        welcome_user = f'Welcome {username}!\n'
        print(welcome_user)
        guest_b.write(welcome_user)
