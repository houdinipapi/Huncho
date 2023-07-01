import os

print("***WELCOME TO SILENT AUCTION***")

# Initializing an empty dictionary
bidder_data = {}


# Function to find winner
def find_winner(bidder_details):
    winner = ""
    highest_bid = 0
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            winner = bidder
    print(f"List of bidders: {bidder_details}")
    print(f"Winner: {winner}\nBid Price: {highest_bid}")


# Flag
end_of_bidding = False

# Running the game in a loop
while not end_of_bidding:
    bidder_name = input("Name: ")
    bidder_price = int(input("Bid: "))
    bidder_data[bidder_name] = bidder_price
    more_bidders = input("Are there more bidders? 'yes' or 'no': ").lower()

    if more_bidders == "no":
        end_of_bidding = True
        find_winner(bidder_data)
    elif more_bidders == "yes":
        # Clearing the screen so that the previous bid cannot be seen.
        os.system("cls")
