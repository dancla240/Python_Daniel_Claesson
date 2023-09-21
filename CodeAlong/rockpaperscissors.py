from random import choice

SIGNS = ['rock','paper','scissors'] # global variabel, alla bokstäver stora betyder att det inte är tänkt att ändras i koden

def main():
    print(f'Welcome to the {", ".join(SIGNS)} game')
    print_rules()
    number_of_rounds = select_number_of_rounds()
    print(f"Best of {number_of_rounds} wins. Let's start!\n")
    game_loop(number_of_rounds)

def print_rules():
    print("Rules: Each player picks a sign: ")
    for winner, loser in zip([0, 1, 2],[2, 0, 1]):
        print(f'{SIGNS[winner].title()} wins over {SIGNS[loser]}')

def select_number_of_rounds():
    while True:
        try:
            rounds = int(input('select number of rounds'))
            if 1 <= rounds <= 10: return rounds
            else: print('Rounds must be between 1 and 10')
                
        except ValueError:
            print('NUmber of rounds must be an integer.')

def game_loop(number_of_rounds):
    for current_round in range(1, number_of_rounds + 1):
        print(f'\nRound {current_round}:')
        sign_player_a = get_sign_from_user()
        sign_player_b = get_sign_from_computer()

        print(f'Computer picks {sign_player_b}.')

        if is_draw(sign_player_a, sign_player_b):
            print('It is a draw.')
        elif wins_over(sign_player_a, sign_player_b):
            print('')
        else:

def is_draw(sign_a, sign_b):
    return sign_a == sign_b: #returnerar True om det är sant
        
def wins_over(sign_a, sign_b):
    for winner, loser in zip([0, 1, 2],[2, 0, 1]):
        if sign_a == SIGNS[winner] and sign_b == SIGNS[loser]: return True

    return False

def get_sign_from_user():
    while True:
        sign = input('Pick a sign: ').strip().lower() #method chaining
        if sign in SIGNS: return sign
        else:
            print(f'You must pick either of {", ".join(SIGNS)}')

def get_sign_from_computer():
    computer = random.choice(SIGNS)
    return computer


main()
