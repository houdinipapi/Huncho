"""
- Implement a program that prompts the user for a str in English
and then outputs the “emojized” version of that str,
converting any codes (or aliases) therein to their corresponding emoji.
"""

import emoji

user_emoji = input("Input: ")
print(f"Output: {emoji.emojize(user_emoji)}")
