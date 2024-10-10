from app.database import engine, metadata  # Importa o engine e a metadata
from app.models.account import accounts  # Importa a tabela de contas
from app.models.transaction import transactions  # Importa a tabela de transações

# Cria todas as tabelas no banco de dados (se ainda não existirem)
def create_db():
    # Cria todas as tabelas definidas na metadata
    metadata.create_all(engine)
    print("Banco de dados e tabelas criados com sucesso!")

if __name__ == "__main__":
    create_db()
