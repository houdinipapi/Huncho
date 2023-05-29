"""
- Implement a program that prompts the user to insert a coin, one at a time,
each time informing the user of the amount due.
- Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
- Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""


def calculate_change(coins):
    total = sum(coins)
    change = total - 50
    return change


def main():
    coins = []
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            coins.append(coin)
            amount_due -= coin

    # change_owed = calculate_change(coins)
    return f"Change Owed: {calculate_change(coins)}"


if __name__ == "__main__":
    print(main())
