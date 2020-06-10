import os
from twilio.rest import Client

account_sid = "acc-sid"
auth_token = "authtoken"

client = Client(account_sid, auth_token)
client.messages.create(
    to="+19732835880",
    from_="+19733148072",
    body="Hello! Welcome to NJ Spine Physical Therapy. Ask to schedule an appintment, hear the office hours, or even get tips for at home excersises to help your injury."
)
