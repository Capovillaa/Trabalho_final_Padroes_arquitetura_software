from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_balance_initial():
    response = client.get("/api/v1/balance")
    assert response.status_code == 200
    assert "balance" in response.json()

def test_create_income_transaction():
    response = client.post(
        "/api/v1/transactions",
        json={"type": "receita", "title": "Venda de Produto", "amount": 100.0}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Transação adicionada com sucesso"}

def test_create_expense_transaction():
    response = client.post(
        "/api/v1/transactions",
        json={"type": "despesa", "title": "Conta de Luz", "amount": 50.0}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Transação adicionada com sucesso"}

def test_create_invalid_transaction():
    response = client.post(
        "/api/v1/transactions",
        json={"type": "invalido", "title": "Erro", "amount": 10.0}
    )
    assert response.status_code == 400
    assert "detail" in response.json()

def test_read_transactions_list():
    response = client.get("/api/v1/transactions")
    assert response.status_code == 200
    transactions = response.json()
    assert isinstance(transactions, list)
    assert len(transactions) >= 2 # Pois inserimos 2 nos testes anteriores
