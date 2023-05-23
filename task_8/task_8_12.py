import random


def game():
    while True:
        text = input('Rock, paper or scissor? (print \'exit\' to end game) ').lower()
        if text in ['scissor', 'rock', 'paper']:
            result = random.choice(['Win', 'Draw', 'Lose'])
            print(result)
        elif text == 'exit':
            return 'Thx for playing!'
        elif text not in ['scissor', 'rock', 'paper']:
            print('Input correct value!')


if __name__ == '__main__':
    print(game())
