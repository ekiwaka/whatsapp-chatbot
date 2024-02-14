from fastapi import FastAPI
from src import chatbot_router

app = FastAPI()
app.include_router(chatbot_router)
