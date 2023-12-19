import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Enter your choice (rock/paper/scissors): ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    return 'computer'

def print_results(winner, user_choice, computer_choice):
    if winner == 'tie':
        print(f'Both players selected {user_choice}. It\'s a tie!')
    elif winner == 'user':
        print(f'{user_choice} beats {computer_choice}. You win!')
    else:
        print(f'{computer_choice} beats {user_choice}. You lose.')

def play_again():
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == 'yes'

def run_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        print_results(winner, user_choice, computer_choice)
        print(f'Score: Player {user_score} - Computer {computer_score}')
        if not play_again():
            break

run_game()