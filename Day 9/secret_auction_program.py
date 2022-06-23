from replit import clear
from art import logo

print(logo)

bids_list = {}
next_bid = True


def findHighestBidder(biddingRecord):
    biggestBid = 0
    for bidder in biddingRecord:
        bid_amount = biddingRecord[bidder]
        if bid_amount > biggestBid:
            biggestBidder = bidder
            biggestBid = bid_amount
    print(f'The winner is {biggestBidder}, with a US${biggestBid} bid.')


while next_bid:
    name = input("What's your name? \n")
    bid = float(input("What's your bid? US$"))
    bids_list[name] = bid
    next_bidder = input("Is there someone else do bid? yes / no \n")
    clear()
    if next_bidder == 'no':
        next_bid = False
        show_result = False
        while not show_result:
            show_result = input('Can we show the winner? yes / no \n')
            if show_result == 'yes':
                show_result = True
                # print(bids_list)
                findHighestBidder(bids_list)
