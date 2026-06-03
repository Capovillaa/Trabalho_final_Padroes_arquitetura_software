# ADR-003: Adotar SQLite como banco de dados embutido

**Status:** Accepted

**Contexto:** O sistema necessita persistir os dados de transações (receitas e despesas) de forma confiável para que o saldo possa ser calculado de maneira consistente entre diferentes execuções. A equipe avaliou a possibilidade de usar bancos de dados relacionais robustos, como PostgreSQL ou MySQL, rodando em contêineres Docker. Contudo, devido  ao prazo restrito, configurar infraestrutura de banco de dados e gerenciar contêineres poderia atrasar o desenvolvimento das regras de negócio e padrões de projeto.

**Decisão:** O sistema utilizará o **SQLite**, configurado no arquivo `finance.db`, adotando o padrão Singleton para garantir o reuso de uma única conexão em toda a aplicação. 

**Consequências:** 
* **Benefícios:** Configuração zero (zero-config). O banco é criado automaticamente no primeiro uso (`create_tables` se não existir). Facilita a portabilidade do projeto para o professor avaliar, pois não requer instalação de serviços de banco de dados.
* **Custos:** O SQLite não lida tão bem com alta concorrência de escritas quanto um SGBD dedicado. Além disso, a aplicação fica acoplada ao sistema de arquivos do servidor. Para os requisitos atuais de um trabalho acadêmico (e o atributo de qualidade de Simplicidade), é a decisão mais acertada.
