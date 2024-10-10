from sqlalchemy import Column, Integer, String, Numeric, Table  # Certifique-se de importar Table
from app.database import metadata, database
from sqlalchemy.orm import relationship

accounts = Table(
    "accounts",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("account_number", String, unique=True, nullable=False),
    Column("balance", Numeric(10, 2), default=0, nullable=False),  # Saldo inicial é 0
    extend_existing=True  # Adicione esta linha
)

class Account:
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, nullable=False)
    balance = Column(Numeric(10, 2), default=0)  # Saldo inicial é 0

    transactions = relationship("Transaction", back_populates="account")
