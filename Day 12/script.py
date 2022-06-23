import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")


def level_chooser():
    game_level = input('Choose your level: type "high" or "easy": ')
    while not game_level == "high" and not game_level == "easy":
        level_chooser()
    if game_level == "high":
        chances = 5
    elif game_level == "easy":
        chances = 10
    return chances


def check_answers(guess_number, target_number):
    if guess_number > target_number:
        print("Too high! \n Guess again: ")
    elif guess_number < target_number:
        print("Too low!\n Guess again: ")
    elif guess_number == target_number:
        print("You won!\n")


def game():

    choosen_number = random.randint(1, 100)
    chances = level_chooser()
    played_number = 0

    while played_number != choosen_number:
        print(f'You have {chances} attempts remaining to guess the number.')
        played_number = int(input('Make a guess: \n'))
        chances -= 1
        check_answers(played_number, choosen_number)

    if input("Want to play again? y / n: ") == "y":
        game()


game()
