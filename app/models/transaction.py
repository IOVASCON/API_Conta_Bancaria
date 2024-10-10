from sqlalchemy import Column, Integer, Numeric, String, ForeignKey, Table
from app.database import metadata  # Ajuste para importar a instância de metadata
from sqlalchemy.orm import relationship

# Definindo a tabela de transações
transactions = Table(
    "transactions",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("amount", Numeric(10, 2), nullable=False),
    Column("transaction_type", String, nullable=False),  # 'deposit' or 'withdraw'
    Column("account_id", Integer, ForeignKey("accounts.id"), nullable=False),
    extend_existing=True  # Adicione isso
)

# Se a classe Transaction for necessária
class Transaction:
    __tablename__ = "transactions"

    account = relationship("Account", back_populates="transactions")
