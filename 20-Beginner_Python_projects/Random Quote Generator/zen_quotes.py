"""
- Scrapes zenquotes website for quotes.
- Generates the quotes randomly.
"""

import os
import requests
import random
from fpdf import FPDF, XPos, YPos

# Ask the user for the file name
filename = input("Filename (without extension): ")

# # Define the path and filename for the PDF file
# pdf_path = os.path.join(r"C:\Users\ADMIN\PycharmProjects\firstProject\Huncho\20-Beginner_Python_projects\Random Quote Generator", "quotes.pdf")

# Define the path and filename for the PDF file
pdf_path = os.path.join(os.getcwd(), f"{filename}.pdf")


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


# Saving the quotes in a PDF file
def save_quotes_to_pdf(quotes, filename):
    pdf = FPDF()

    # Set up the PDF document
    pdf.set_font('helvetica', size=12)
    pdf.add_page()

    # # Clear existing content
    # pdf.set_xy(0, 0)
    # pdf._out('')

    # Write each quote to the PDF
    for quote in quotes:
        pdf.cell(0, 10, txt=quote, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Save the PDF file
    pdf.output(f"{filename}.pdf")


# Load existing quotes from the PDF file
existing_quotes = []
try:
    with open(pdf_path, "rb") as file:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        existing_quotes = file.read().decode("latin-1").splitlines()
except FileNotFoundError:
    pass

# Generate new quotes
new_quotes = []
for _ in range(5):  # --> Generate 5 new quotes
    quote = random_quote()
    new_quotes.append(quote)

# Save new quotes to the PDF file
save_quotes_to_pdf(new_quotes, filename)

# # Print the new_quotes --> Prints in the terminal
# for quote in new_quotes:
#     print(quote)
