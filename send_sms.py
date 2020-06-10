import os
from twilio.rest import Client

account_sid = "AC1f248038fc29be70d3c6d48fbc63256b"
auth_token = "f77e1de681dae9ebd199ea9449d58e79"

client = Client(account_sid, auth_token)
client.messages.create(
    to="+19732835880",
    from_="+19733148072",
    body="Hello! Welcome to NJ Spine Physical Therapy. Ask to schedule an appintment, hear the office hours, or even get tips for at home excersises to help your injury."
)