# Author: Bailey Bakerson <bakerso1@msu.edu>
import os
from twilio.rest import Client

class twii:
  # Set environment variables for your credentials
  # Read more at http://twil.io/secure
  account_sid = None
  auth_token = None
  client = None

  def __init__(self) -> None:
    self.account_sid = "AC0137bd72aca87c825774d2e95707b694"
    # self.auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    self.client = Client(self.account_sid, self.auth_token)


  def send_msg(self, msg = "No Mesage Given", num_to = "+12696359755", num_from = "+12693994156"):
    message = self.client.messages.create(
      body=msg,
      from_=num_from,
      to=num_to
    )

    #send it
    message.sid