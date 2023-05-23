# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC2fa8bce99d406f8222fea32c97df1319"
auth_token = "ae93d5f5beacd6b2fe1498c4ef36c7ec"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+12543182623",
  to="+254719504161"
)
print(message.sid)
