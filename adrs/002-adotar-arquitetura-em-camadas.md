# ADR-002: Adotar Arquitetura em Camadas (Layered Architecture)

**Status:** Accepted

**Contexto:** O trabalho exige a aplicação rigorosa de princípios SOLID e Clean Code. Misturar a lógica de acesso ao banco de dados, regras de negócio de finanças e o tratamento de rotas web no mesmo arquivo criaria um alto acoplamento. Precisamos de uma organização interna que isole o domínio da aplicação da tecnologia web adotada.

**Decisão:** O backend do sistema adotará a Arquitetura em Camadas (Layered Architecture), dividida estritamente em:
1. **Rotas (Controllers):** Lida com as requisições HTTP (FastAPI).
2. **Serviços (Domain/Business):** Contém a lógica de cálculo e manipulação de transações.
3. **Repositórios (Data Access):** Abstrai as consultas ao banco de dados SQLite.

**Consequências:** * **Benefícios:** Alto grau de manutenibilidade e testabilidade. Permite trocar a biblioteca web ou o banco de dados no futuro com impacto mínimo nas regras de negócio financeiras.
* **Custos:** Introduz a necessidade de criar mais arquivos e interfaces no início do projeto, gerando um pouco de *boilerplate* (código repetitivo de infraestrutura).