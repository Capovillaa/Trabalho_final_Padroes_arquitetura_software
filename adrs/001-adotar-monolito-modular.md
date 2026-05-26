# ADR-001: Adotar Monolito Modular como Arquitetura Macro

**Status:** Accepted

**Contexto:** O projeto requer o desenvolvimento de um sistema de gestão financeira com um escopo bem delimitado e um prazo de entrega bastante curto (cerca de duas semanas). A equipe de desenvolvimento é reduzida. O uso de uma arquitetura distribuída (como microsserviços) adicionaria uma carga excessiva de complexidade de infraestrutura, testes e deploy, o que desviaria o foco da aplicação correta dos padrões de projeto e regras de negócio.

**Decisão:** O sistema será desenvolvido como um Monolito Modular, concentrando o frontend (arquivos estáticos) e a API (backend) em uma única unidade implantável de deploy.

**Consequências:** * **Benefícios:** Maior facilidade para desenvolver, testar e realizar o deploy inicial. Elimina a necessidade de lidar com latência de rede entre serviços ou consistência eventual de dados.
* **Custos:** Se o sistema crescer enormemente no futuro, a escalabilidade de partes específicas será mais difícil, exigindo a escalabilidade de todo o sistema. Para o contexto atual, é um trade-off perfeitamente aceitável.