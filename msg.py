# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC14f51bc1b84eceb2b5e916bd9932a6c9"
auth_token = "165453036d8632c43725a504f835e05c"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+2348111623853",
    from_="+14582219586",
    body="Hello there!")
