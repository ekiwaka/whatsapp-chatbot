from pydantic import BaseModel


class DataModel(BaseModel):
    message: str
    sender: str
    receiver: str
