from twilio.rest import Client
account_sid = 'ACddcb72e963042a33ed6d64ec34f5e669'
auth_token = '4a63f7811b06e2c6f79c78ff3e0e9fdd'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+1 928 263 6846',
    to='+8613661451627',
    body="goodbye",
)


