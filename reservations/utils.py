import os
from twilio.rest import Client
import dramatiq

account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

def send_sms(phone_number, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_= "+17608402283",
        to=phone_number
    )
    return message

