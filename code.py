# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
# function to get the highest bidder.
def highest_bidder(bidding_dict):

    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"the winner is {winner} with a bid of ${highest_bid}")


bid_dict = {}
continue_bidding = True

while continue_bidding:
    name = input("Enter your name: \n")
    bid = int(input("Enter your price: \n"))
    bid_dict[name] = bid

    should_cont = input("are there any other bidders? type yes or no.\n").lower()

    if should_cont == 'no':
        continue_bidding = False
        highest_bidder(bid_dict)
        # print(bid_dict)

    elif should_cont == 'yes':
        print("\n" * 50)

