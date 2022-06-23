'''
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

    Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
'''

print('Welcome to the Love Calculator!')

name1 = input("What's your name? ").lower()
name2 = input("What's their name? ").lower()

concatenated_name = name1 + name2

t = concatenated_name.count('t')
r = concatenated_name.count('r')
u = concatenated_name.count('u')
e = concatenated_name.count('e')

true = t + r + u + e

l = concatenated_name.count('l')
o = concatenated_name.count('o')
v = concatenated_name.count('v')
e = concatenated_name.count('e')

love = l + o + v + e

love_score = true + love

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 or love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
