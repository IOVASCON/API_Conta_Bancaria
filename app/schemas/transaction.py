from pydantic import BaseModel, PositiveFloat
from datetime import datetime
from enum import Enum

class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"

class TransactionIn(BaseModel):
    account_id: int
    type: TransactionType
    amount: PositiveFloat

class TransactionOut(BaseModel):
    id: int
    account_id: int
    type: TransactionType
    amount: PositiveFloat
    timestamp: datetime

    class Config:
        orm_mode = True
