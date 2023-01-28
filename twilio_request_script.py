# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC0137bd72aca87c825774d2e95707b694"
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello from Twilio",
  from_="+18559971746",
  to="+12696359755"
)

print(message.sid)