"""
- This a sample program for a random quote generator.
- The quotes are already in a list, so the program will
    randomly pick the choices.
"""
import random


# Creating the random_quote function
def random_quote():
    quotes = [
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The secret of getting ahead is getting started. - Mark Twain",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The best way to predict the future is to create it. - Peter Drucker",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    ]

    return random.choice(quotes)


print(random_quote())
