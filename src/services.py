from src.models import TransactionFactory
from src.strategies import IncomeStrategy, ExpenseStrategy
from src.repository import ITransactionRepository

class TransactionService:
    def __init__(self, repository: ITransactionRepository):
        self.repository = repository
        # Mapa de estratégias (Strategy Pattern dinâmico)
        self.strategies = {
            "receita": IncomeStrategy(),
            "despesa": ExpenseStrategy()
        }

    def add_transaction(self, type: str, title: str, amount: float):
        transaction = TransactionFactory.create_transaction(type, title, amount)
        self.repository.save(transaction)
        return {"message": "Transação adicionada com sucesso"}

    def get_balance(self):
        transactions = self.repository.get_all_amounts_and_types()

        balance = 0.0

        for amount, transaction_type in transactions:
            strategy = self.strategies.get(transaction_type)
            if strategy:
                balance = strategy.calculate(balance, amount)

        return {"balance": balance}

    def get_all_transactions(self):
        return self.repository.get_all()