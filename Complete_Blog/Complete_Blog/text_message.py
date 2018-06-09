from twilio.rest import TwilioRestClient

account_sid = "AC03bf9ab146d977a3e16d54df93b5ccf4"
auth_token = "3726d2130e257628a55c67a013f9662e"
my_cell = "+919616475722"
my_twilio = "+14084795523"


def send_text_message(my_msg):
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
    return message
