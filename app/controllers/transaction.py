from fastapi import APIRouter
from app.schemas.transaction import TransactionIn
from app.services.transaction import TransactionService

router = APIRouter()
transaction_service = TransactionService()

@router.post("/")
async def create_transaction(transaction: TransactionIn):
    return await transaction_service.create(transaction)
