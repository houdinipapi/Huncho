"""
Slices an email into different parts
"""


def email_slicer():
    user_email = input("Your Email: ")
    (username, main_domain) = user_email.split('@')
    (domain, extension) = main_domain.split('.')

    return f"Username: {username}\nMain Domain: {main_domain}\nDomain: {domain}\nExtension: {extension}\n"


print(email_slicer())
