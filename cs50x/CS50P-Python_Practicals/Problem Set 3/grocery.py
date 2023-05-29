"""
- Implement a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one’s input to a program).
- Then output the user’s grocery list in all uppercase,
sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
- No need to pluralize the items.
- Treat the user’s input case-insensitively.
"""

user_list = list()
try:
    while True:
        user_input = input().strip().lower()
        user_list.append(user_input)
except EOFError:
    pass
user_dict = {user_input: user_list.count(user_input) for user_input in user_list}
for user_input, count in sorted(user_dict.items()):
    print(count, user_input.upper())
