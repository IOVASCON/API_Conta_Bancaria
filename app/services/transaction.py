from databases.interfaces import Record
from app.models.transaction import Transaction  # Corrigido para importar a classe Transaction
from app.models.account import Account  # Corrigido para importar a classe Account
from app.database import database
from app.schemas.transaction import TransactionIn
from app.exceptions import AccountNotFoundError, BusinessError

class TransactionService:
    async def create(self, transaction: TransactionIn) -> Record:
        # Verificando se a conta existe
        account = await database.fetch_one(Account.select().where(Account.c.id == transaction.account_id))
        if not account:
            raise AccountNotFoundError("Account not found")

        # Calculando o novo saldo
        if transaction.transaction_type == "withdraw":
            new_balance = account.balance - transaction.amount
            if new_balance < 0:
                raise BusinessError("Insufficient funds")
        else:
            new_balance = account.balance + transaction.amount

        # Registrando a transação e atualizando o saldo
        await database.execute(Transaction.insert().values(
            account_id=transaction.account_id,
            transaction_type=transaction.transaction_type,
            amount=transaction.amount
        ))
        await database.execute(Account.update().where(Account.c.id == transaction.account_id).values(balance=new_balance))
        
        # Retornando a transação registrada
        return await database.fetch_one(Transaction.select().where(Transaction.c.account_id == transaction.account_id))
