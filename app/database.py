import databases
import sqlalchemy as sa
from app.config import settings

# Criação da instância do banco de dados
database = databases.Database(settings.database_url)

# Definição da metadata
metadata = sa.MetaData()

# Definição da tabela de contas
accounts = sa.Table(
    "accounts",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True, index=True),
    sa.Column("account_number", sa.String, unique=True, nullable=False),
    sa.Column("balance", sa.Numeric(10, 2), default=0)  # Saldo inicial é 0
)

# Definição da tabela de transações
transactions = sa.Table(
    "transactions",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True, index=True),
    sa.Column("amount", sa.Numeric(10, 2), nullable=False),
    sa.Column("transaction_type", sa.String, nullable=False),  # 'deposit' ou 'withdraw'
    sa.Column("account_id", sa.Integer, sa.ForeignKey("accounts.id"), nullable=False),
)

# Criação do engine para interagir com o banco de dados
engine = sa.create_engine(settings.database_url, connect_args={"check_same_thread": False})

# Função para criar as tabelas no banco de dados
def create_tables():
    metadata.create_all(engine)

# Inicializa a conexão do banco de dados
async def connect():
    await database.connect()

# Encerra a conexão do banco de dados
async def disconnect():
    await database.disconnect()
