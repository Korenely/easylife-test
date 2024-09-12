from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str

class TransactionCreate(BaseModel):
    transaction_type: str
    amount: float
