from src.database import DatabaseConnection
from src.models import TransactionFactory
from src.strategies import IncomeStrategy, ExpenseStrategy

class TransactionService:
    def __init__(self):
        
        self.db = DatabaseConnection().get_connection()

    def add_transaction(self, type: str, title: str, amount: float):
       
        transaction = TransactionFactory.create_transaction(type, title, amount)

        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO transactions (title, amount, type) VALUES (?, ?, ?)",
            (transaction.title, transaction.amount, transaction.get_type())
        )
        self.db.commit()
        return {"message": "Transação adicionada com sucesso"}

    def get_balance(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT amount, type FROM transactions")
        transactions = cursor.fetchall()

        balance = 0.0
        income_strategy = IncomeStrategy()
        expense_strategy = ExpenseStrategy()

        for amount, type in transactions:
            
            if type == "receita":
                balance = income_strategy.calculate(balance, amount)
            elif type == "despesa":
                balance = expense_strategy.calculate(balance, amount)

        return {"balance": balance}

    def get_all_transactions(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT id, title, amount, type FROM transactions")
        
        return [{"id": row[0], "title": row[1], "amount": row[2], "type": row[3]} for row in cursor.fetchall()]