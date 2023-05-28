"""
- Implement a program that prompts the user for names, one per line, until the user inputs control-d.
- Assume that the user will input at least one name.
- Then bid adieu to those names,
    separating two names with one and,
    three names with two commas and one and,
    and names with commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""

import sys
import inflect

delimiter = inflect.engine()  # --> Acts as a delimiter when joining strings

names_list = list()

while True:
    try:
        names = input("Name: ").title()
        if len(names) < 1:
            sys.exit("No Input")

        names_list.append(names)
        output = delimiter.join(names_list)

    except EOFError:
        print("\n")
        print("Adieu, adieu, to " + output)
        break
    else:
        continue
