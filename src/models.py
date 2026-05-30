from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, title: str, amount: float):
        self.title = title
        self.amount = amount

    @abstractmethod
    def get_type(self) -> str:
        pass

class Income(Transaction):
    def get_type(self) -> str:
        return "receita"

class Expense(Transaction):
    def get_type(self) -> str:
        return "despesa"

class TransactionFactory:
    @staticmethod
    def create_transaction(type: str, title: str, amount: float) -> Transaction:
        """
        Retorna a classe correta baseada no tipo passado como parâmetro
        """
        if type.lower() == "receita":
            return Income(title, amount)
        elif type.lower() == "despesa":
            return Expense(title, amount)
        else:
            # Tratamento de erros explícito (Clean Code)
            raise ValueError("Tipo inválido. Use 'receita' ou 'despesa'.")