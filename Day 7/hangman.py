import random

lifes = 5
guesses = 0
correct_letters = 0
word_list = ['pedra', 'amor', 'chapeu', 'computador']
chosen_word = random.choice(word_list)
print(chosen_word)

blank_word = []

for letter in chosen_word:
    blank_word.append("_")

print(f'The word has {len(chosen_word)} letters: {blank_word}')

chosen_letter = input("Guess a letter: ").lower()

for letter in chosen_word:
    if chosen_letter == letter:
        blank_word.replace(blank_word[letter], letter)
    else:
        print('wrong')


