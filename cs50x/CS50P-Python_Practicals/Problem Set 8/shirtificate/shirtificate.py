"""
- Implement a program that prompts the user for their name and outputs,
    using 'fpdf2', a CS50 shirtificate in a file called 'shirtificate.pdf'.
- Specifications:
    - The orientation of the PDF should be Portrait.
    - The format of the PDF should be A4, which is 210mm wide by 297mm tall.
    - The top of the PDF should say "CS50 Shirtificate" as text,
    centered horizontally.
    - The shirt's image should be centered horizontally.
    - The user's name should be on top of the shirt, in white text.
"""

from fpdf import FPDF, XPos, YPos


class CS50Shirtificate(FPDF):
    def header(self):
        # Set the font and print the header at the top of each page
        self.set_font('helvetica', 'B', 16)
        self.cell(0, 10, 'CS50 Shirtificate', align='C')
        self.ln(20)  # --> MOve down by 20 units

    def footer(self):
        # Set the footer's font and position
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)

        # Print the page number in the footer
        self.cell(0, 10, 'Page %s' % self.page_no(), align='C')

    def generate_shirtificate(self, name):
        # Add a new page with Portrait orientation and A4 format
        self.add_page(orientation='P', format='A4')

        # Add the shirt image at the center of the page
        self.image('shirtificate.png', x=self.w / 2 - 65, y=self.h / 2 - 90, w=130, h=180)

        # Set the text color to white
        self.set_text_color(255, 255, 255)

        # Set the font and size for the name
        self.set_font('helvetica', 'B', 24)

        # Calculate the position to center the name on the shirt
        self.set_xy(self.w / 2 - 50, self.h / 2 - 90)

        # Print the name with centered alignment
        self.cell(100, 20, name, border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

        # Output the generated shirtificate as a PDF file
        self.output('shirtificate.pdf')


def main():
    name = input("Name: ")
    shirtificate = CS50Shirtificate()
    shirtificate.generate_shirtificate(name + " took CS50")


if __name__ == "__main__":
    main()
