"""
- Retrieves quotes from an online site, using web scraping.
- Outputs the quotes retrieved randomly.
"""

import requests
from bs4 import BeautifulSoup
import random


def random_quote():
    # Send a GET request to the website
    response = requests.get("https://example.com/quotes")

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the HTML elements that contain the quotes
    quote_elements = soup.find_all("blockquote")

    # Extract the text of each quote --> List comprehension
    quotes = [quote.get_text().strip() for quote in quote_elements]

    # Select a random quote from the list
    return random.choice(quotes)


print(random_quote())
