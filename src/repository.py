from abc import ABC, abstractmethod
from src.database import DataBaseConnection
from src.models import Transaction

class ITransactionRepository(ABC):
    @abstractmethod
    def save(self, transaction: Transaction):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_all_amounts_and_types(self):
        pass

class SQLiteTransactionRepository(ITransactionRepository):
    def __init__(self, db_connection: DataBaseConnection):
        self.db = db_connection.get_connection()

    def save(self, transaction: Transaction):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO transactions (title, amount, type) VALUES (?, ?, ?)",
            (transaction.title, transaction.amount, transaction.get_type())
        )
        self.db.commit()

    def get_all(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT id, title, amount, type FROM transactions")
        return [{"id": row[0], "title": row[1], "amount": row[2], "type": row[3]} for row in cursor.fetchall()]

    def get_all_amounts_and_types(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT amount, type FROM transactions")
        return cursor.fetchall()
