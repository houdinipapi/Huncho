"""
This program sends email to a user using Python
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from app_code import pass_code

# Set up email sender information
email_sender = "ochiengcliff.co@gmail.com"
email_password = pass_code
email_recipient = "taved91664@larland.com"

# Set up message information
subject = "Test Email"
body = """
This a is a test email.
Let's see what it can do.
"""
attachment_file = "sample.pdf"
image_file = "example.png"

# Set up message
