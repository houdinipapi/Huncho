from twilio.rest import Client
from auth_details import Account_SID
from auth_details import Auth_Token
from auth_details import Phone_Number

# Twilio account SID and authorization token
account_sid = Account_SID
auth_token = Auth_Token

# Creating a Twilio Client
client = Client(account_sid, auth_token)


def send_message(to_phone_number, message):
    try:
        # Sending the message
        message = client.messages.create(
            body=message,
            from_=Phone_Number,
            to=to_phone_number
        )
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")


# Example Application
phone_number = input("Enter your phone number: ")
message_text = input("Type your message:\n")


send_message(phone_number, message_text)
