import random

def game():

    print('''Welcome to Rock, Paper, Scissors!
 Enter your choice:
 1. Rock
 2. Paper
 3. Scissors''')

    choices = ['rock', 'paper', 'scissors']
    player_choice = int(input('Your choice (1-3): ')) - 1

    if player_choice < 0 or player_choice > 2:
        return 'Invalid choice. Please try again.'

    computer_choice = random.randint(0, 2)

    print(f'You chose: {choices[player_choice]} \nComputer chose: {choices[computer_choice]}')

    win_comb = ((player_choice == 0 and computer_choice == 2)
                or (player_choice == 1 and computer_choice == 0)
                or (player_choice == 2 and computer_choice == 1))

    if player_choice == computer_choice:
        return 'It\'s a tie!'
    elif win_comb:
        return 'Congratulations! You win!'
    return 'Sorry, you lose!'


if __name__ == '__main__':
    print(game())
