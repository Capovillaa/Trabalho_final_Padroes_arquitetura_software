from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.services import TransactionService
from src.database import DataBaseConnection
from src.repository import SQLiteTransactionRepository

app = FastAPI(
    title="FinanceLite API",
    description="API REST para gestão financeira",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db_connection = DataBaseConnection()
repository = SQLiteTransactionRepository(db_connection)
service = TransactionService(repository)

# DTO (Data Transfer Object): Valida a entrada de dados (Prática de Clean Code)
class TransactionInput(BaseModel):
    type: str
    title: str
    amount: float

@app.post("/api/v1/transactions")
def create_transaction(data: TransactionInput):
    try:
        return service.add_transaction(data.type, data.title, data.amount)
    except ValueError as e:
       
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/v1/transactions")
def list_transactions():
    return service.get_all_transactions()

@app.get("/api/v1/balance")
def get_current_balance():
    return service.get_balance()