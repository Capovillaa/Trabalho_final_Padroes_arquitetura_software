# ADR-006: Introduzir Padrão Repository e Injeção de Dependência

**Status:** Accepted (Modifica e complementa o ADR-002)

**Contexto:** Durante o desenvolvimento inicial do sistema, adotamos a Arquitetura em Camadas (ADR-002). No entanto, percebemos um "code smell": a camada de Serviços (`TransactionService`) estava fortemente acoplada ao banco de dados SQLite, instanciando a conexão diretamente e executando comandos SQL (`INSERT`, `SELECT`) junto com as regras de negócio. Isso violava o Princípio de Inversão de Dependência (DIP) do SOLID e prejudicava a testabilidade do sistema, além de contradizer a própria promessa de uma "camada de acesso a dados" isolada.

**Decisão:** Decidimos refatorar o código para introduzir o Padrão *Repository*. Criamos a interface abstrata `ITransactionRepository` e a implementação concreta `SQLiteTransactionRepository`. Além disso, alteramos o `TransactionService` para não instanciar mais o banco de dados; em vez disso, a dependência do repositório é injetada via construtor durante a inicialização na camada de rotas (`main.py`).

**Consequências:**
* **Benefícios:** Adequação perfeita ao Princípio de Inversão de Dependência (DIP). A camada de negócios (Services) agora está completamente isolada de detalhes de infraestrutura (SQLite). O código tornou-se muito mais limpo e favorável a testes unitários (pois agora o repositório pode ser "mockado").
* **Custos:** O refatoramento exigiu a criação de novos arquivos e a alteração da forma como os objetos são instanciados na raiz da aplicação. Adiciona uma ligeira complexidade na inicialização (`main.py`), mas o ganho estrutural compensa amplamente esse custo.
