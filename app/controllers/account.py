from fastapi import APIRouter, Depends
from app.schemas.account import AccountIn, AccountOut
from app.schemas.transaction import TransactionOut
from app.services.account import AccountService
from app.services.transaction import TransactionService

router = APIRouter()

# Inicializando os serviços
account_service = AccountService()
transaction_service = TransactionService()

@router.post("/", response_model=AccountOut)
async def create_account(account: AccountIn):
    """
    Endpoint para criar uma nova conta.
    """
    return await account_service.create(account)

@router.get("/")
async def read_accounts(limit: int = 10, skip: int = 0):
    """
    Endpoint para obter uma lista de contas com suporte à paginação.
    """
    return await account_service.read_all(limit, skip)

@router.get("/{id}/transactions", response_model=list[TransactionOut])
async def read_account_transactions(id: int, limit: int, skip: int = 0):
    """
    Endpoint para obter transações de uma conta específica.
    """
    return await transaction_service.read_all(account_id=id, limit=limit, skip=skip)
