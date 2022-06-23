# Password Generator Project
# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(
    input("How many letters would you like in your password? Maximum: 52\n"))
nr_symbols = int(input(f"How many symbols would you like? Maximum: 9\n"))
nr_numbers = int(input(f"How many numbers would you like? Maximum: 10\n"))

password_letters = []
password_numbers = []
password_symbols = []
randomized = []

for i in range(0, nr_letters):
    password_letters.append(letters[round(random.random() * len(letters) - 1)])

for i in range(0, nr_numbers):
    password_numbers.append(numbers[round(random.random() * len(numbers) - 1)])

for i in range(0, nr_symbols):
    password_symbols.append(symbols[round(random.random() * len(symbols) - 1)])

consolidated = (password_letters + password_numbers + password_symbols)

for i in consolidated:
    sort = random.randint(0, len(consolidated) - 1)
    randomized.append(consolidated.pop(sort))

print(randomized)
