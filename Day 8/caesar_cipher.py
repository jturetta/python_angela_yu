# ENCRYPT

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

# DECRYPT

# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# e.g.
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
# print output: "The decoded text is hello"

# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# encrypt(plain_text=text, shift_amount=shift)

import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# alphabet is duplicated because "out of index" in some letters close to the end of list!

# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


# def encrypt(plain_text, shift_amount):
#     cipher_text = ''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f'The encoded text is {cipher_text}')


# def decrypt(cipher_text, shift_amount):
#     plain_text = ''
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f'The decoded text is {plain_text}')


# if direction == 'encode':
#     encrypt(text, shift)
# elif direction == 'decode':
#     decrypt(text, shift)

# IMPROVED CODE

def caesar(direction, text, shift_amount):
    output_text = ''
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == 'encode':
                new_position = position + shift_amount
            elif direction == 'decode':
                new_position = position - shift_amount
            output_text += alphabet[new_position]
        else:
            output_text += letter
    print(f'The {direction}d text is {output_text}\n')


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n")) % 26
    caesar(direction, text, shift_amount)
    answer = input('Do you want to try again? yes / no \n')
    if answer == 'yes':
        should_continue
    else:
        should_continue = False
        print('*** Goodbye ***')
# END
