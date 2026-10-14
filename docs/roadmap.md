# Roadmap de desenvolvimento — Aporte

## Objetivo

Desenvolver o Aporte progressivamente, priorizando correção financeira, simplicidade, explicabilidade e testes automatizados.

O roadmap distingue a implementação do núcleo matemático da comparação de produtos financeiros reais. O primeiro não depende de fontes externas; o segundo exige condições específicas de cada produto e dados adequados.

Uma funcionalidade só deve ser marcada como concluída quando estiver implementada, testada e documentada.

## Fase 1 — Fundação matemática e domínio

**Objetivo:** estabelecer uma base confiável para os cálculos financeiros.

### Tarefas

- [x] Revisar a estrutura inicial do projeto.
- [x] Definir as responsabilidades de domínio, serviços de aplicação e API.
- [x] Substituir `float` por `Decimal` nos cálculos monetários.
- [x] Definir regras de validação de domínio.
- [x] Definir convenções de taxas e períodos suportadas pelo cálculo genérico.
- [x] Documentar a fórmula de juros compostos e suas limitações.
- [x] Implementar testes para casos usuais e entradas inválidas.
- [x] Garantir que o domínio possa ser testado sem iniciar a API.

### Critério de conclusão

O cálculo genérico de juros compostos deverá produzir resultados verificáveis, com precisão e convenções documentadas.

## Fase 2 — Comparador genérico de cenários

**Objetivo:** permitir comparar duas alternativas matemáticas antes de introduzir regras específicas de produtos financeiros.

### Tarefas

- [ ] Definir o modelo de entrada de cada cenário.
- [ ] Receber capital inicial, taxa efetiva anual e prazo.
- [ ] Exigir capital inicial e prazo equivalentes para a comparação direta.
- [ ] Calcular o montante bruto estimado de cada cenário.
- [ ] Calcular o rendimento bruto estimado de cada cenário.
- [ ] Calcular a diferença absoluta entre os montantes.
- [ ] Expor o comparador por meio da API.
- [ ] Definir schemas de entrada e saída.
- [ ] Criar testes de integração da API.
- [ ] Documentar as premissas e limitações do resultado.

### Critério de conclusão

O usuário deverá conseguir enviar dois cenários, receber os resultados calculados e compreender que a comparação não considera impostos, custos, inflação, risco ou variações futuras das taxas.

## Fase 3 — Modelagem de produtos financeiros

**Objetivo:** representar produtos reais sem confundir suas características contratuais com os indicadores de mercado.

### Prioridade inicial

1. Tesouro Selic.
2. CDB pós-fixado.

### Tarefas

- [ ] Definir o modelo de domínio dos produtos.
- [ ] Distinguir produto, indexador, taxa contratual e observação de mercado.
- [ ] Representar condições de remuneração.
- [ ] Representar vencimento e liquidez, quando aplicáveis.
- [ ] Representar emissor e informações relevantes de risco de crédito.
- [ ] Definir os dados mínimos necessários para calcular cada produto.
- [ ] Documentar as limitações dos modelos iniciais.
- [ ] Criar testes específicos para cada categoria suportada.

### Critério de conclusão

O domínio deverá representar Tesouro Selic e CDB pós-fixado de maneira distinta, sem depender de um único modelo genérico de taxa anual constante.

## Fase 4 — Regras financeiras dos produtos

**Objetivo:** calcular resultados de produtos reais com convenções compatíveis com suas características.

### Tarefas

- [ ] Documentar as convenções de remuneração de cada categoria.
- [ ] Definir o tratamento de períodos e dias úteis quando necessário.
- [ ] Definir a aplicação de taxas pós-fixadas.
- [ ] Identificar regras tributárias aplicáveis.
- [ ] Identificar custos relevantes.
- [ ] Distinguir resultado bruto de resultado líquido.
- [ ] Definir como apresentar dados insuficientes.
- [ ] Criar testes com exemplos financeiros verificáveis.

### Critério de conclusão

Cada produto suportado deverá produzir resultados coerentes com as regras implementadas e informar as limitações da simulação.

## Fase 5 — Dados de mercado e persistência

**Objetivo:** permitir que o comparador utilize dados históricos rastreáveis.

### Tarefas

- [ ] Identificar fontes oficiais para Selic, CDI/DI e IPCA.
- [ ] Documentar as séries e suas convenções.
- [ ] Implementar a obtenção de dados públicos.
- [ ] Registrar fonte, período de referência e momento da coleta.
- [ ] Tratar duplicações e correções.
- [ ] Definir critérios para identificar dados desatualizados.
- [ ] Introduzir PostgreSQL quando a persistência se tornar necessária.
- [ ] Definir o modelo de persistência e suas migrações.
- [ ] Criar testes para dados inválidos ou indisponíveis.

### Critério de conclusão

Os dados utilizados deverão ter origem e período de referência identificáveis, e o comparador deverá funcionar com dados históricos disponíveis localmente.

## Fase 6 — Comparação ampliada de investimentos

**Objetivo:** ampliar a comparação para além de taxas hipotéticas constantes.

### Tarefas

- [ ] Incorporar tributação e custos para os produtos suportados.
- [ ] Calcular rentabilidade líquida estimada.
- [ ] Incorporar inflação quando houver dados e premissas compatíveis.
- [ ] Adicionar Tesouro Prefixado.
- [ ] Adicionar Tesouro IPCA+.
- [ ] Distinguir taxa contratada de retorno efetivamente observado.
- [ ] Considerar oscilações de preço antes do vencimento, quando aplicável.
- [ ] Exibir premissas, limitações e dados utilizados.
- [ ] Implementar cenários alternativos de taxas futuras.

### Critério de conclusão

As comparações deverão apresentar resultados coerentes com o produto, o período e as premissas utilizadas, sem sugerir garantias de rentabilidade.

## Fase 7 — Carteira e objetivos financeiros

**Objetivo:** considerar a situação do investidor ao avaliar novos aportes.

### Tarefas

- [ ] Modelar carteiras e posições.
- [ ] Permitir cadastro manual de investimentos.
- [ ] Distinguir valores informados, calculados e observados.
- [ ] Modelar objetivos financeiros.
- [ ] Implementar análise de concentração por categoria, emissor e indexador.
- [ ] Permitir simular novos aportes.
- [ ] Avaliar compatibilidade entre prazo, liquidez e objetivos.
- [ ] Sinalizar informações insuficientes.
- [ ] Preservar as premissas das simulações importantes.

### Critério de conclusão

O sistema deverá explicar como um novo aporte pode alterar a composição da carteira e sua compatibilidade com os objetivos informados.

## Fase 8 — Interface e experiência do usuário

**Objetivo:** oferecer uma interface acessível para as funcionalidades já validadas.

### Tarefas

- [ ] Avaliar os fluxos de uso da API documentada.
- [ ] Definir as principais telas e fluxos.
- [ ] Implementar uma interface web quando o domínio estiver suficientemente estável.
- [ ] Integrar a interface à API.
- [ ] Exibir cálculos, premissas e limitações.
- [ ] Garantir que a interface não replique as regras financeiras do backend.

### Critério de conclusão

O usuário deverá conseguir executar os fluxos suportados sem precisar interagir diretamente com endpoints ou estruturas internas.

## Fase 9 — Evoluções futuras

Estas funcionalidades não fazem parte do MVP inicial e só deverão ser consideradas após a validação do núcleo.

- [ ] Regras mais sofisticadas de diversificação.
- [ ] Mais categorias de investimentos.
- [ ] Análises históricas e comparações ampliadas.
- [ ] Modelos probabilísticos de cenários.
- [ ] Aprendizado de máquina, caso exista um problema que justifique seu uso.
- [ ] Integrações externas opcionais.
- [ ] Sincronização ou hospedagem remota, caso compatíveis com os objetivos de privacidade.

## Princípios de execução

1. Não avançar para cálculos específicos de produtos antes de documentar suas convenções.
2. Não introduzir banco de dados antes de haver uma necessidade clara de persistência.
3. Não depender de dados externos para validar cálculos matemáticos básicos.
4. Não marcar uma funcionalidade como concluída apenas porque o endpoint responde.
5. Não misturar projeções com resultados observados.
6. Não introduzir aprendizado de máquina para substituir regras determinísticas ainda não validadas.
7. Manter PRD, roadmap, regras financeiras e testes coerentes entre si.

## Relação com a documentação

- `PRD.md` define os requisitos e o escopo do produto.
- `docs/architecture.md` define a organização técnica.
- `docs/domain-model.md` define os conceitos do domínio.
- `docs/financial-rules.md` define as fórmulas e convenções.
- `docs/decisions/` registra decisões arquiteturais importantes.

O roadmap deverá ser atualizado quando houver mudanças relevantes no escopo, na ordem de implementação ou nos critérios de conclusão.
