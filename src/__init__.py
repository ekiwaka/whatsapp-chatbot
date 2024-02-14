from fastapi import APIRouter
from src.chatbot import send_message
from src.data_model import DataModel
from dotenv import load_dotenv
import os

load_dotenv()
chatbot_router = APIRouter()

@chatbot_router.post("/send-message")
async def send_message_endpoint(data: DataModel):
    account_sid = os.getenv("account_sid")
    auth_token = os.getenv("auth_token")
    return await send_message(data.message, data.sender, data.receiver, account_sid, auth_token)
