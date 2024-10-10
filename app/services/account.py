from databases.interfaces import Record
from app.models.account import Account
from app.database import database, accounts  # Importar a variável 'accounts'
from app.schemas.account import AccountIn

class AccountService:
    async def create(self, account: AccountIn) -> Record:
        query = accounts.insert().values(account_number=account.account_number, balance=account.balance)  # Certifique-se de que account.account_number e account.balance estão corretos
        account_id = await database.execute(query)
        return await database.fetch_one(accounts.select().where(accounts.c.id == account_id))

    async def read_all(self, limit: int, skip: int = 0) -> list[Record]:
        query = accounts.select().limit(limit).offset(skip)
        return await database.fetch_all(query)
