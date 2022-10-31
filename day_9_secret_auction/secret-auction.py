import imp
import os
clear = lambda: os.system('clear')


from art import logo
print(logo)

# name = input("What is your name? ")
# price = int(input("What's your bid? "))
# should_continue = input("Are there any other users who want to bid? ")
bids = {}
blind_auction_in_progress = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winnder is {winner} with a bid of ${highest_bid}")

while blind_auction_in_progress:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")

    if should_continue == 'yes':
        clear()
    elif should_continue == 'no':
        blind_auction_in_progress = False
        find_highest_bidder(bids)



