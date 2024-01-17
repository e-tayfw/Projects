from twilio.rest import Client
import os

ACCOUNT_SID = os.environ.get("ENV_TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("ENV_TWILIO_AUTH_TOKEN")
VIRTUAL_NUMBER = "+14157669096"
ACTUAL_NUMBER = "+6591690715"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=VIRTUAL_NUMBER,
            to=ACTUAL_NUMBER,
        )
        print(message.status)
