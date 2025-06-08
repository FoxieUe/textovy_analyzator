"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Marek Procházka
email: pokefuck@icloud.com
"""
import random
WORD_DIVIDER = "-" * 47

def get_secret_number():
    number_option = [
        "0", "1", "2", "3", "4",
        "5", "6", "7", "8", "9"
    ]
    while True:
        random.shuffle(number_option)
        if number_option[0] != "0":
            chosen_number = "".join(number_option[0:4])
            return chosen_number

def get_valid_input():
    while True:
        x = input(f">>> ")
        if not x.isdigit():
            print(f"Please use only numbers\n{WORD_DIVIDER}")
        elif len(set(x)) != 4:
            print(f"Choose 4 different numbers\n{WORD_DIVIDER}")  
        elif x[0] == "0":
            print(f"Your number can not start with 0\n{WORD_DIVIDER}")
        else:
            return x        

def count_bulls_and_cows(secret_guess, player_guess):
    cows = 0
    bulls = 0
    player_rest = list()
    secret_rest = list()
    for sg, pg in zip(secret_guess, player_guess):
        if sg == pg:
            bulls += 1
        else:
            secret_rest.append(sg)
            player_rest.append(pg)
    for digit in player_rest:
        if digit in secret_rest:
            cows += 1
            secret_rest.remove(digit)
    return bulls, cows
    
def play_game():
    print("Hi there!")
    print(WORD_DIVIDER)
    print(
        f"I've generated a random 4 digit number for you.\n"
        f"Let's play a bulls and cows game.\n"
        f"{WORD_DIVIDER}\nEnter a Number:\n{WORD_DIVIDER}"
    )

    chosen_number = get_secret_number()
    try_counter = 0

    while True:
        player_guess = list(get_valid_input())
        secret_guess = list(chosen_number)
        bulls, cows = count_bulls_and_cows(secret_guess, player_guess)
    
        if bulls == 4:
            try_counter += 1
            guess_text = "guess" if try_counter == 1 else "guesses"
            print(
                f"Correct, you've guessed the right number"
                f"\nin {try_counter} {guess_text}!"
            )
            break
        else:
            try_counter += 1
            bull_text = "bull" if bulls == 1 else "bulls"
            cow_text = "cow" if cows == 1 else "cows"
            print(
                f"{bulls} {bull_text}, {cows} {cow_text}"
                f"\n{WORD_DIVIDER}"
            )
play_game()