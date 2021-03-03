"""
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. 

Then use that number to print out Heads or Tails.
"""

import random

player1 = random.randint(1, 2)
player2 = random.randint(1, 2)
coin = random.randint(1, 2)

if player1 == 1:
    player1 = "head"
elif player1 == 2:
    player1 = "tail"

if player2 == 1:
    player2 = "head"
elif player2 == 2:
    player2 = "tail"

if coin == 1:
    coin = "head"
elif coin == 2:
    coin = "tail"

if player1 == coin and player2 == coin:
    print(
        f"Nobody wins! Coin was {coin}, Player 1 was {player1} and Player2 was {player2}."
    )
elif player1 != coin and player2 != coin:
    print(
        f"Nobody wins! Coin was {coin}, Player 1 was {player1} and Player2 was {player2}."
    )
elif player1 == coin and player2 != coin:
    print(
        f"Player 1 wins! Coin was {coin}, Player 1 was {player1} and Player2 was {player2}."
    )
elif player1 != coin and player2 == coin:
    print(
        f"Player 2 wins! PCoin was {coin}, layer 1 was {player1} and Player2 was {player2}."
    )
