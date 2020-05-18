from twilio.rest import Client

account_sid = 'AC4c8462ab827f67c37bfcb219f3840293'
auth_token = '16267a3e3fbe5850fcccb4c822ddffcf'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12057827118',
    body='message',
    to='+5562985429500'
)

print(message.sid)
