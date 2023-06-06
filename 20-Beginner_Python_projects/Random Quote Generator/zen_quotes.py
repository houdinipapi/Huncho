"""
- Scrapes zenquotes website for quotes.
- Generates the quotes randomly.
"""

import requests
import random


def random_quote():
    # Send a GET request to the Zen Quotes API
    response = requests.get("https://zenquotes.io/api/random")

    # Parse the JSON response
    data = response.json()

    # Extract the quote and author from the response
    quote = data[0]['q']
    author = data[0]['a']

    # Format the quote and author
    formatted_quote = f"{quote} - {author}"

    return formatted_quote


print(random_quote())
