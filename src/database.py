import sqlite3

class DataBaseConnection:

    """
    Padrão Singleton: garante que apenas uma instancia de conexão 
    com o banco seja criada durante toda a execução do programa.
    """

    _instance = None

    def __new__(cls):
        
        if cls._instance is None:

            cls._instance = super(DataBaseConnection, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect("finance.db",check_same_thread=False)
            cls._instance._create_tables()

        return cls._instance
    
    def _create_tables(self):

        """Cria tabelas de transações se ela não existir"""

        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                amount REAL NOT NULL,
                type TEXT NOT NULL
            )
        """)

        self.connection.commit()

    def get_connection(self):
        return self.connection