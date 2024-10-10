# app/exceptions.py

class AccountNotFoundError(Exception):
    """Exceção lançada quando uma conta não é encontrada."""
    pass

class BusinessError(Exception):
    """Exceção para erros de negócio."""
    pass
