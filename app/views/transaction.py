from pydantic import BaseModel
from datetime import datetime

class TransactionOut(BaseModel):
    id: int
    account_id: int
    type: str
    amount: float
    timestamp: datetime
