import random
from replit import clear
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
print(' ')  # just for space between logo and first line

lifes = 7
guesses = 0
correct_letters = 0

chosen_word = random.choice(word_list)
# print(chosen_word)

display = []
for letter in chosen_word:
    display.append("_")

print(f'The word has {len(chosen_word)} letters: {display}')

while lifes > 0:
    chosen_letter = input("Guess a letter: ").lower()
    clear()
    if chosen_letter in display:
        print(f"You've already guessed the letter {chosen_letter}")
        print(stages[lifes - 1])
    else:
        for position in range(len(chosen_word)):
            if chosen_letter == chosen_word[position]:
                display[position] = chosen_letter
                guesses += 1
                print('NICE ONE!')
                print(stages[lifes - 1])
    if chosen_letter not in chosen_word:
        lifes -= 1
        print(stages[lifes - 1])
        print('WRONG ONE!')
    print(display)
    if lifes == 0:
        print(stages[lifes])
        print('*** GAME OVER ***')
        print(f'The right word is: {chosen_word}')
        break
    elif guesses == len(chosen_word):
        print('*** YOU WIN ***')
        print(f'The right word is: {chosen_word}')
