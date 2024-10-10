from pydantic import BaseModel, PositiveFloat
from datetime import datetime

class AccountIn(BaseModel):
    user_id: int
    balance: PositiveFloat

class AccountOut(BaseModel):
    id: int
    user_id: int
    balance: float
    created_at: datetime

    class Config:
        orm_mode = True
