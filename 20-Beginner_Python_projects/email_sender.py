"""
This program sends email to a user using Python
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# from email.mime.application import MIMEApplication
from app_code import pass_code

# Set up email sender information
# email_sender = "olivertim.ot@gmail.com"
email_sender = input("Your Email: ")
email_password = pass_code
# email_recipient = "taved91664@larland.com"
email_recipient = input("RECIPIENT: ")

# Set up message information
subject = input("SUBJECT:")
body = input("Body: ")

# attachment_file = "sample.pdf"
# image_file = "example.png"

# Set up message
message = MIMEMultipart()
message["From"] = email_sender
message["To"] = email_recipient
message["Subject"] = subject

# Add message body
message.attach(MIMEText(body, "plain"))

# # Add attachment
# with open(attachment_file, "rb") as attachment:
#     attach_part = MIMEApplication(attachment.read(), _subtype="pdf")
#     attach_part.add_header("Content-Disposition", f"attachment; filename={attachment_file}")
#     message.attach(attach_part)
#
# # Add image
# with open(image_file, "rb") as image:
#     img_part = MIMEImage(image.read(), _subtype="png")
#     img_part.add_header("Content-Disposition", f"attachment; filename={image_file}")
#     message.attach(img_part)

# Set up SMTP server and send message
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_recipient, message.as_string())

print("Email sent successfully!")
