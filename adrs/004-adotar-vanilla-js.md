# ADR-004: Adotar Vanilla JS e HTML/CSS Puro no Frontend

**Status:** Accepted

**Contexto:** Ao fazer o projeto, precisamos decidir como construir a interface de usuário que se comunique com a API REST. Há uma tendência atual em utilizar frameworks e bibliotecas SPA (Single Page Application) como React, Vue ou Angular. O problema é que a disciplina avalia especificamente os padrões e a arquitetura do software de maneira geral. A adoção de um framework de frontend complexo traria consigo a necessidade de ferramentas de build (Node.js, Webpack/Vite) e uma curva de aprendizado que desviaria o foco do objetivo principal.

**Decisão:** O frontend do FinanceLite será construído inteiramente utilizando **Vanilla JavaScript, HTML5 e CSS3 nativo**, concentrado em um único arquivo `index.html` (com os estilos e scripts embutidos na página).

**Consequências:**
* **Benefícios:** Máxima simplicidade. Qualquer pessoa pode abrir o arquivo `index.html` no navegador e utilizar o sistema sem precisar executar um `npm install` ou configurar um servidor frontend. A comunicação com o backend é feita nativamente via `fetch API`.
* **Custos:** À medida que o frontend cresce, a ausência de componentes reutilizáveis ou gerência de estado formal (como Redux/Context API) torna a manutenção do `index.html` mais complexa (o código pode ficar um pouco "espaguete"). Para o escopo deste trabalho, o tamanho reduzido da interface absorve bem essa complexidade.
