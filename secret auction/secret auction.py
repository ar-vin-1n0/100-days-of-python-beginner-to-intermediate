import os

def highest_bid(bids):
    high_bid = 0
    highest_bidder = 0
    for key, value in bids.items():
        if value > high_bid:
            high_bid = value
            highest_bidder = key
    return {highest_bidder: high_bid}

bids = {}

bids_ongoing = True
while bids_ongoing:
    name = input("Enter your name: ")
    bid_amount = float(input("Enter your bid amount: "))
    bids[name] = bid_amount


    finish_bid = input("anyone else to bid [y/n]: ")
    if finish_bid == "y":
        print("\n" * 50)
    elif finish_bid == "n":
        print("Thank you for your time")
        print("bids are closed")
        bids_ongoing = False

winner = highest_bid(bids)

winner_name = list(winner.keys())[0]
winner_amount = list(winner.values())[0]

print(f"{winner_name} wins with a bid of ₹{winner_amount}")



