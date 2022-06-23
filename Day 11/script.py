import random
from replit import clear
from art import logo

def dealCard():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the calculated score of them."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, computer_score):
    if player_score == 0 or player_score > 21:
        return "Computer wins"
    elif computer_score == 0 or computer_score > 21:
        return "You win"
    elif player_score > computer_score:
        return "You win"
    elif computer_score > player_score:
        return "Computer wins"
    else:
        return "draw"


def playGame():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Each player needs to get 2 cards
    for _ in range(2):
        user_cards.append(dealCard())
        computer_cards.append(dealCard())


    # Loop while player wants to keep playing
    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f'Your cards: {user_cards}, Your score: {user_score}')
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            while computer_score != 0 and computer_score < 17:
                computer_cards.append(dealCard())
                computer_score = calculate_score(computer_cards)

            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(dealCard())
            else:
                is_game_over = True

        print (f" Your final hand: {user_cards}, final score: {user_score}")
        print (f" Computer's final hand: {computer_cards}, final score: {computer_score}")
        print (compare (user_score, computer_score))

        play_again = input("Would you like to play again? Type 'y' or 'n': ")
        if play_again == "y":
            clear()
            playGame()

