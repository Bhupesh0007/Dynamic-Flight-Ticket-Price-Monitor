from twilio.rest import Client

class NotificationManager:

    def __init__(self):
        self.client = Client("username", "password")

    def send_sms(self, message_body):      
        message = self.client.messages.create(
            from_="your twilio number",
            body=message_body,
            to="your number"
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{"your twilio number"}',
            body=message_body,
            to=f'whatsapp:{"your number"}'
        )
        print(message.sid)
