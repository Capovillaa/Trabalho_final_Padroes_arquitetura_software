import pytest
from fastapi.testclient import TestClient
from src.main import app, service
from src.repository import ITransactionRepository
from src.models import Transaction

class MockRepository(ITransactionRepository):
    def __init__(self):
        self.transactions = []

    def save(self, transaction: Transaction):
        self.transactions.append(transaction)

    def get_all(self):
        return [
            {"id": i+1, "title": t.title, "amount": t.amount, "type": t.get_type(), "category": t.category, "date": t.date}
            for i, t in enumerate(self.transactions)
        ]

    def get_all_amounts_and_types(self):
        return [(t.amount, t.get_type()) for t in self.transactions]

mock_repo = MockRepository()
service.repository = mock_repo

client = TestClient(app)

@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    
    mock_repo.transactions = []
    yield

def test_read_balance_initial():
    response = client.get("/api/v1/balance")
    assert response.status_code == 200
    assert response.json() == {"balance": 0.0}

def test_create_income_transaction():
    response = client.post(
        "/api/v1/transactions",
        json={"type": "receita", "title": "Venda", "amount": 100.0, "category": "Vendas", "date": "2023-10-01"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Transação adicionada com sucesso"}
    assert len(mock_repo.transactions) == 1

def test_create_expense_transaction():
    response = client.post(
        "/api/v1/transactions",
        json={"type": "despesa", "title": "Conta", "amount": 50.0, "category": "Contas", "date": "2023-10-02"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Transação adicionada com sucesso"}

def test_create_invalid_transaction():
    response = client.post(
        "/api/v1/transactions",
        json={"type": "invalido", "title": "Erro", "amount": 10.0, "category": "Erro", "date": "2023-10-03"}
    )
    assert response.status_code == 400
    assert "detail" in response.json()

def test_read_transactions_list():
    
    client.post("/api/v1/transactions", json={"type": "receita", "title": "Venda", "amount": 100.0, "category": "Vendas", "date": "2023-10-01"})
    client.post("/api/v1/transactions", json={"type": "despesa", "title": "Conta", "amount": 50.0, "category": "Contas", "date": "2023-10-02"})
    
    response = client.get("/api/v1/transactions")
    assert response.status_code == 200
    transactions = response.json()
    assert len(transactions) == 2
