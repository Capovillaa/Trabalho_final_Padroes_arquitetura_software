# Diagramas do Projeto FinanceLite

Aqui estão os diagramas em código Mermaid solicitados pelo professor. Você pode copiá-los e colá-los em ferramentas como o [Mermaid Live Editor](https://mermaid.live/) para gerar as imagens, ou diretamente no seu documento se a ferramenta suportar (como Notion, Obsidian ou extensões do VSCode).

## 1. Arquitetura Macro (Estilo C4 - Componentes/Containers)

```mermaid
graph TD
    subgraph "Monolito Modular (FinanceLite)"
        UI["Frontend\n(index.html / Vanilla JS)"]
        API["Backend API\n(Rotas FastAPI)"]
        Services["Serviços de Domínio\n(TransactionService)"]
        Repo["Acesso a Dados\n(TransactionRepository)"]
        DB["Banco de Dados\n(SQLite / finance.db)"]
    end
    UI -- "HTTP GET/POST\n(Fetch API)" --> API
    API -- "Delega Regras" --> Services
    Services -- "Grava/Consulta" --> Repo
    Repo -- "Executa SQL" --> DB
```

## 2. Diagrama de Classes (Foco nos Padrões GoF)

```mermaid
classDiagram
    class DataBaseConnection {
        -_instance
        +__new__()
        +_create_tables()
        +get_connection()
    }
    note for DataBaseConnection "Padrão: Singleton"

    class Transaction {
        <<abstract>>
        +title: str
        +amount: float
        +get_type()* str
    }
    class Income {
        +get_type() str
    }
    class Expense {
        +get_type() str
    }
    Transaction <|-- Income
    Transaction <|-- Expense

    class TransactionFactory {
        +create_transaction(type, title, amount) Transaction$
    }
    note for TransactionFactory "Padrão: Factory Method"
    TransactionFactory ..> Transaction : instancia

    class CalculationStrategy {
        <<abstract>>
        +calculate(current_balance, amount)* float
    }
    class IncomeStrategy {
        +calculate(current_balance, amount) float
    }
    class ExpenseStrategy {
        +calculate(current_balance, amount) float
    }
    CalculationStrategy <|-- IncomeStrategy
    CalculationStrategy <|-- ExpenseStrategy
    note for CalculationStrategy "Padrão: Strategy"

    class ITransactionRepository {
        <<interface>>
        +save(transaction)
        +get_all()
        +get_all_amounts_and_types()
    }
    class SQLiteTransactionRepository {
        -db
        +save(transaction)
        +get_all()
        +get_all_amounts_and_types()
    }
    ITransactionRepository <|.. SQLiteTransactionRepository
    SQLiteTransactionRepository --> DataBaseConnection : usa

    class TransactionService {
        -repository: ITransactionRepository
        -strategies: dict
        +add_transaction()
        +get_balance()
    }
    TransactionService --> ITransactionRepository : usa (Injeção)
    TransactionService --> TransactionFactory : usa
    TransactionService --> CalculationStrategy : usa
```

## 3. Diagrama de Sequência (Fluxo Central: Adicionar Transação)

```mermaid
sequenceDiagram
    actor Usuario
    participant UI as Frontend (Vanilla JS)
    participant API as API (main.py)
    participant Svc as TransactionService
    participant Factory as TransactionFactory
    participant Repo as SQLiteTransactionRepository
    participant DB as SQLite (database.py)

    Usuario->>UI: Preenche formulário e clica "Lançar"
    UI->>API: HTTP POST /api/v1/transactions (JSON)
    API->>Svc: add_transaction(type, title, amount)
    Svc->>Factory: create_transaction(type, title, amount)
    Factory-->>Svc: Retorna instância (Income ou Expense)
    Svc->>Repo: save(transaction)
    Repo->>DB: INSERT INTO transactions...
    DB-->>Repo: Confirma persistência
    Repo-->>Svc: Operação concluída
    Svc-->>API: {"message": "Transação adicionada..."}
    API-->>UI: 200 OK
    UI-->>Usuario: Atualiza interface (recarrega lista e saldo)
```
