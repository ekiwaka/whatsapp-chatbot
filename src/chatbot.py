from typing import Union
from twilio.rest import Client

async def send_message(message: str, sender: str, receiver: str, account_sid: str, auth_token: str) -> str:
    client = Client(account_sid, auth_token)
    client.messages.create(
        from_=sender,
        body=message,
        to=receiver
    )
    return await generate_response(message)

async def generate_response(message: str) -> str:
    return f"You said: {message}"
