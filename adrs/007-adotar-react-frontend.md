# ADR-007: Adotar React para o Frontend

**Status:** Accepted

**Contexto:** O projeto FinanceLite iniciou utilizando Vanilla JS para o frontend (conforme ADR-004), mantendo máxima simplicidade sem build tools. No entanto, o sistema evoluiu para exigir visualizações de dados mais complexas, como dashboards iterativos e gráficos para despesas e receitas. O uso de Vanilla JS puro com manipulação direta de DOM se torna custoso e difícil de manter em interfaces ricas (estilo Apple, com componentes reativos).

**Decisão:** Adotar a biblioteca **React** (via Vite) para a construção do frontend. O React traz um modelo robusto de componentização e estado reativo, além de ecossistema vasto (ex: Recharts para os gráficos). 

**Consequências:**
* **Benefícios:** Maior facilidade para construir UIs complexas e dashboards interativos. Código do frontend estruturado em componentes, melhorando a manutenibilidade e escalabilidade (clean code no client-side).
* **Custos:** Necessidade de processo de build (Node.js + Vite) e gerenciamento de pacotes (`npm`). Aumenta o número de dependências do projeto. A ADR-004 fica obsoleta e é substituída por esta decisão.
