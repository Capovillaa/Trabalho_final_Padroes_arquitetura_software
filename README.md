# Trabalho_final_Padroes_arquitetura_software
# FinanceLite 

Sistema simples e eficiente para gestão de finanças pessoais, desenvolvido como projeto acadêmico para aplicação de padrões de Arquitetura de Software.

## Objetivos
O sistema permite registrar receitas e despesas, calculando o saldo atual do usuário. O projeto foca na demonstração de conceitos como:
* Arquitetura em Camadas (Layered Architecture)
* Padrões GoF (Factory, Strategy, Singleton)
* Princípios SOLID e Clean Code
* Documentação de API com OpenAPI

## Stack Tecnológica
* **Backend:** Python + FastAPI
* **Banco de Dados:** SQLite
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)

## Como executar

### Pré-requisitos
* Python 3.8+ instalado na máquina.

### Backend (API REST)
1. Abra o terminal na pasta raiz do projeto (`Trabalho_final_Padroes_arquitetura_software`).
2. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
   *Caso prefira instalar manualmente, execute: `pip install fastapi uvicorn pydantic`*

4. Execute o servidor FastAPI usando o Uvicorn:
   ```bash
   uvicorn src.main:app --reload
   ```
5. A API estará rodando em `http://127.0.0.1:8000`. Você pode acessar a documentação interativa (Swagger UI) em `http://127.0.0.1:8000/docs`.

### Frontend
1. Como o frontend usa HTML/CSS/JS (Vanilla) puro, basta abrir o arquivo `index.html` em qualquer navegador web.
2. Certifique-se de que a API (Backend) esteja em execução para que as operações funcionem perfeitamente.

### Testes Automatizados
Para verificar a integridade da API e a aplicação das regras de negócio, o projeto conta com testes automatizados utilizando `pytest`.
1. Certifique-se de que o ambiente virtual está ativado e as dependências instaladas.
2. Na raiz do projeto, defina o diretório atual como raiz do Python e execute o `pytest`:
   ```bash
   # No Windows (PowerShell):
   $env:PYTHONPATH="."; pytest src/test_main.py
   
   # No Linux/Mac:
   PYTHONPATH=. pytest src/test_main.py
   ```
