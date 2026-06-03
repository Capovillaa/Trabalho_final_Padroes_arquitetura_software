# ADR-005: Utilizar FastAPI para o Design da API REST

**Status:** Accepted

**Contexto:** O projeto exige a exposição de uma API formalmente especificada com design REST e documentada com OpenAPI. Em Python, existem diversos frameworks web maduros, como Django ou Flask. Precisamos de uma solução que permita o desenvolvimento rápido de rotas web focadas em REST, que possua alta performance e que automatize a geração da documentação OpenAPI sem trabalho adicional de configuração.

**Decisão:** O backend será desenvolvido utilizando o **FastAPI** como framework web e `Pydantic` para a validação dos DTOs (Data Transfer Objects).

**Consequências:**
* **Benefícios:** O FastAPI atende perfeitamente ao requisito da disciplina ao gerar automaticamente a especificação OpenAPI (Swagger UI disponível na rota `/docs`). Ele incentiva boas práticas e tipagem (Clean Code) através da integração nativa com o Pydantic, garantindo validação explícita das entradas (`TransactionInput`). Além disso, possui excelente performance graças ao ASGI.
* **Custos:** Exige que a equipe tenha familiaridade com os *Type Hints* (tipagem) do Python. Além disso, o gerenciamento de dependências e banco de dados deve ser construído manualmente, pois o framework não traz um ORM embutido (o que resolvemos aplicando a Arquitetura em Camadas, conforme ADR-002, e o padrão Singleton para o banco, conforme ADR-003).
