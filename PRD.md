# Aporte — Product Requirements Document (PRD)

**Versão:** 0.5  
**Status:** Em desenvolvimento  
**Tipo de projeto:** Open-source, local-first  
**Licença:** MIT  
**Última atualização:** 14 de outubro de 2026

## 1. Visão geral

O Aporte é uma plataforma open-source de inteligência de investimentos destinada a auxiliar investidores pessoas físicas na comparação de produtos financeiros, na compreensão de suas carteiras e no planejamento de novos aportes.

A plataforma busca responder inicialmente a uma pergunta simples:

> Dadas duas alternativas de investimento, qual apresenta o maior montante estimado para o mesmo capital e horizonte temporal, considerando as premissas adotadas?

Em etapas posteriores, o Aporte ampliará essa análise para considerar tributação, custos, inflação, liquidez, risco, diversificação e objetivos financeiros.

O projeto terá uma abordagem local-first: os dados pessoais e os cálculos deverão permanecer sob controle do usuário, sem depender de um serviço centralizado para executar as funcionalidades essenciais.

O desenvolvimento priorizará regras determinísticas, cálculos verificáveis e explicações compreensíveis. Inteligência artificial e aprendizado de máquina não fazem parte do MVP inicial.

## 2. Problema

A comparação entre investimentos pode ser difícil porque produtos aparentemente semelhantes apresentam diferenças de remuneração, indexação, tributação, liquidez, vencimento e risco.

Comparar apenas as taxas anunciadas pode levar a conclusões inadequadas. Uma taxa maior não implica necessariamente maior retorno líquido, melhor preservação do poder de compra ou maior compatibilidade com as necessidades do investidor.

O Aporte pretende reduzir essa dificuldade por meio de cálculos reproduzíveis, premissas explícitas e análises progressivamente mais completas.

## 3. Público-alvo

### 3.1 Público principal

Investidores pessoas físicas que desejam:

- Compreender como diferentes taxas afetam o montante investido.
- Comparar alternativas de investimento sob premissas compatíveis.
- Aprender a interpretar produtos de renda fixa.
- Considerar fatores além da rentabilidade nominal.
- Planejar aportes de maneira mais fundamentada.

### 3.2 Público secundário

Desenvolvedores e colaboradores interessados em software financeiro open-source, educação financeira e cálculos verificáveis.

## 4. Objetivos do produto

1. Implementar cálculos financeiros básicos, verificáveis e testáveis.
2. Comparar dois cenários de investimento para o mesmo capital e horizonte.
3. Evoluir o comparador para produtos financeiros reais.
4. Manter histórico de indicadores de mercado utilizados nos cálculos.
5. Permitir o cadastro manual de uma carteira.
6. Simular como novos aportes podem afetar a carteira e os objetivos do usuário.
7. Explicar os fatores que influenciam cada resultado.
8. Preservar a privacidade dos dados e permitir execução local.
9. Estabelecer uma arquitetura extensível sem introduzir complexidade prematuramente.

## 5. Princípios do produto

- **Explicabilidade:** apresentar os critérios e as premissas que influenciam cada resultado.
- **Reprodutibilidade:** os mesmos dados, premissas e versões das regras devem produzir resultados equivalentes.
- **Correção financeira:** documentar e testar as convenções utilizadas.
- **Transparência:** distinguir dados observados, valores informados e projeções.
- **Privacidade:** manter os dados pessoais locais por padrão.
- **Separação de responsabilidades:** manter as regras financeiras independentes da API, do banco de dados e da interface.
- **Evolução incremental:** adicionar funcionalidades quando houver uma necessidade definida.
- **Ausência de garantias:** não apresentar projeções como resultados futuros garantidos.

## 6. Escopo do MVP

O desenvolvimento será incremental. O primeiro incremento validará os cálculos e a comparação de cenários genéricos antes da implementação completa de produtos financeiros reais.

### 6.1 F01 — Cálculos financeiros básicos

O sistema deverá:

- Receber capital inicial, taxa efetiva anual e prazo.
- Calcular o montante segundo a fórmula de juros compostos.
- Calcular o rendimento bruto estimado.
- Validar entradas inválidas e limites definidos.
- Adotar representação decimal apropriada para valores monetários.
- Possuir testes automatizados.
- Documentar as unidades e convenções utilizadas.

O cálculo genérico será uma ferramenta matemática inicial. Não deverá ser apresentado como modelo completo de todos os produtos financeiros.

### 6.2 F02 — Comparador genérico de dois cenários

O sistema deverá permitir que o usuário informe duas alternativas de investimento hipotéticas.

Cada alternativa deverá possuir:

- Capital inicial.
- Taxa efetiva anual.
- Prazo de aplicação.

Para uma comparação direta, as duas alternativas deverão utilizar o mesmo capital inicial e o mesmo horizonte temporal.

O sistema deverá apresentar:

- Montante bruto estimado da alternativa A.
- Montante bruto estimado da alternativa B.
- Rendimento bruto estimado de cada alternativa.
- Diferença absoluta entre os montantes.
- Identificação de qual cenário apresenta o maior montante, quando houver diferença.
- Premissas e limitações do cálculo.

O sistema não deverá interpretar automaticamente o maior montante como recomendação de investimento.

O comparador inicial não considerará impostos, custos, inflação, risco de crédito, liquidez ou variações futuras das taxas. Essas limitações deverão ser visíveis ao usuário.

### 6.3 F03 — Cadastro de produtos financeiros

Após a validação do comparador genérico, o domínio deverá evoluir para representar produtos financeiros reais.

As primeiras categorias prioritárias serão:

1. Tesouro Selic.
2. CDB pós-fixado.

Em etapas posteriores, poderão ser incluídos:

3. Tesouro Prefixado.
4. Tesouro IPCA+.

Os atributos de cada produto deverão ser específicos à sua categoria, incluindo, conforme aplicável:

- Nome e categoria.
- Emissor.
- Indexador.
- Taxa ou condição contratual.
- Data de vencimento.
- Condições de liquidez.
- Informações sobre tributação e custos.
- Dados de referência e suas fontes.

O sistema deverá distinguir o produto financeiro do indicador utilizado como referência. Por exemplo, um CDB remunerado a 103% do CDI é um produto com determinada condição contratual; o CDI é um indicador de mercado.

### 6.4 F04 — Comparação de produtos financeiros

O comparador deverá evoluir para utilizar regras específicas de cada produto.

A comparação deverá considerar, conforme a categoria e os dados disponíveis:

- Capital inicial equivalente.
- Mesmo horizonte temporal.
- Montante bruto estimado.
- Rendimento bruto estimado.
- Tributação e custos aplicáveis.
- Rentabilidade líquida estimada.
- Liquidez e vencimento.
- Riscos relevantes.
- Efeito da inflação, quando aplicável.

As condições utilizadas deverão ser compatíveis com o período de análise. Quando não for possível fazer uma comparação confiável, o sistema deverá informar as limitações ou indicar que o resultado é inconclusivo.

O sistema não deverá aplicar indiscriminadamente a mesma fórmula a todos os produtos.

### 6.5 F05 — Histórico de indicadores de mercado

O sistema deverá preparar uma camada de dados históricos para indicadores relevantes à análise de investimentos brasileiros.

Prioridades iniciais:

- Selic.
- CDI/DI.
- IPCA.

Taxas de títulos públicos e informações da curva de juros poderão ser incorporadas posteriormente.

Cada observação deverá registrar, quando disponível:

- Indicador.
- Data ou período de referência.
- Valor e unidade.
- Convenção aplicável.
- Fonte dos dados.
- Momento da coleta.
- Informações necessárias para identificar correções ou atualizações.

A aplicação deverá permitir atualizar os dados públicos de forma controlada. Inicialmente, a verificação poderá ocorrer sob demanda ou na inicialização, sem exigir um serviço de atualização contínua.

### 6.6 F06 — Cadastro manual de carteira

O usuário deverá poder registrar suas posições sem integrar contas bancárias ou corretoras.

O modelo deverá evoluir para representar:

- Produto associado à posição.
- Valor investido ou quantidade.
- Data de aquisição.
- Vencimento e condições relevantes.
- Valor atual informado ou calculado.
- Informações necessárias para estimar rendimento.

O sistema deverá distinguir valores informados pelo usuário de valores calculados ou obtidos de fontes externas.

### 6.7 F07 — Objetivos financeiros

O usuário deverá poder registrar objetivos financeiros, incluindo:

- Nome e finalidade.
- Valor pretendido.
- Prazo ou data-alvo.
- Valor já reservado, quando informado.
- Necessidade de liquidez e restrições relevantes.

Inicialmente, a análise de objetivos será independente de recomendações automáticas de alocação. A associação entre posições e objetivos poderá ser feita manualmente.

### 6.8 F08 — Análise de carteira e aportes

Em etapas posteriores, o sistema deverá permitir:

- Avaliar a composição da carteira.
- Identificar concentrações por categoria, emissor e indexador, quando os dados permitirem.
- Simular diferentes alocações para um novo aporte.
- Avaliar a compatibilidade entre investimentos e objetivos.
- Explicar os fatores favoráveis e desfavoráveis de cada cenário.
- Sinalizar dados insuficientes para uma conclusão confiável.

A análise deverá utilizar regras determinísticas e explicáveis. Uma alternativa com maior rentabilidade estimada não deverá ser considerada automaticamente a melhor.

### 6.9 F09 — Testes e validação

Os cálculos e as regras deverão possuir testes automatizados, incluindo progressivamente:

- Casos usuais.
- Entradas inválidas e valores extremos.
- Limites de taxas e períodos.
- Precisão decimal e arredondamento.
- Conversões de taxas.
- Contagem de dias úteis, quando implementada.
- Tributação e custos, quando implementados.
- Dados ausentes, atualizados ou corrigidos.
- Reprodutibilidade das simulações.

## 7. Requisitos não funcionais

### RNF01 — Execução local

O núcleo deverá funcionar localmente sem exigir hospedagem externa para executar cálculos sobre dados disponíveis localmente.

### RNF02 — Privacidade

Os dados pessoais da carteira não deverão ser enviados a serviços externos por padrão. A obtenção de dados públicos de mercado não deverá transmitir informações pessoais desnecessárias.

### RNF03 — Precisão financeira

Cálculos monetários deverão utilizar representação decimal apropriada, convenções documentadas e regras explícitas de arredondamento.

### RNF04 — Testabilidade

As regras de negócio deverão poder ser testadas sem iniciar a API, acessar a internet ou depender de um banco de dados.

### RNF05 — Integridade histórica

Os dados de mercado deverão manter informações suficientes para identificar sua origem e período de referência. Correções não deverão apagar silenciosamente a rastreabilidade necessária.

### RNF06 — Segurança

Credenciais, segredos e configurações locais não deverão ser versionados no repositório.

### RNF07 — Manutenibilidade

O domínio financeiro deverá permanecer separado da API, da persistência e da interface.

### RNF08 — Documentação

O escopo, as decisões técnicas, as convenções financeiras e as limitações deverão ser documentados e atualizados com a implementação.

## 8. Regras e restrições financeiras

1. Rentabilidade passada não garante rentabilidade futura.
2. Rentabilidade nominal, líquida e real são conceitos distintos.
3. Selic e CDI/DI não devem ser tratados como indicadores idênticos.
4. Produtos diferentes exigem convenções de cálculo compatíveis com suas condições.
5. Valores estimados não devem ser apresentados como resultados observados.
6. Dados ausentes não devem ser tratados silenciosamente como zero.
7. Uma taxa hipotética constante não deve ser confundida com uma previsão de taxas futuras.
8. Um resultado matemático maior não implica necessariamente melhor adequação ao investidor.
9. As comparações deverão explicitar as premissas e limitações relevantes.
10. O sistema não deverá executar ordens de investimento no MVP.

As fórmulas, convenções de taxas, tributação e custos deverão ser documentados em `docs/financial-rules.md`.

## 9. Fora do escopo do MVP inicial

- Integração com Open Finance.
- Conexão automática a contas bancárias ou corretoras.
- Execução de ordens ou movimentação de dinheiro.
- Plataforma hospedada com sincronização em nuvem.
- Modelos de aprendizado de máquina.
- Previsão de preços ou garantia de rentabilidade futura.
- Cobertura de todos os produtos financeiros existentes.
- Análise completa de carteiras e objetivos na primeira entrega.
- Automatização avançada de tarefas agendadas.
- Aplicativo móvel nativo.

Esses itens poderão ser reconsiderados após a validação das funcionalidades essenciais.

## 10. Modelo conceitual

O domínio deverá evoluir progressivamente para contemplar:

- **Cenário de investimento:** parâmetros de uma simulação financeira.
- **Produto financeiro:** características e condições de um produto.
- **Indicador de mercado:** taxa ou índice utilizado como referência.
- **Observação de mercado:** valor de um indicador em uma data ou período.
- **Posição de carteira:** participação do investidor em determinado produto.
- **Carteira:** agrupamento das posições de um investidor.
- **Objetivo financeiro:** meta, prazo e valor pretendido.
- **Simulação de aporte:** parâmetros e alternativas avaliadas.
- **Resultado de simulação:** resultados calculados e premissas correspondentes.

A implementação deverá ser incremental e acompanhada por `docs/domain-model.md`.

## 11. Arquitetura e tecnologias

A arquitetura inicial será um monólito modular.

### Backend

- Python.
- FastAPI.
- Pydantic.
- pytest.

### Persistência e análise de dados

- PostgreSQL em uma etapa posterior.
- SQLAlchemy e Alembic quando a persistência for introduzida.
- pandas e NumPy quando forem úteis para análise de séries históricas e dados tabulares.

### Interface

Uma interface web com Next.js, React e TypeScript poderá ser adicionada posteriormente. A API deverá permitir essa integração sem transferir as regras financeiras para a interface.

### Separação de responsabilidades

O domínio financeiro não deverá depender diretamente do FastAPI, do banco de dados ou da interface. Os serviços de aplicação coordenarão os casos de uso, enquanto a infraestrutura ficará responsável por persistência e comunicação externa.

Decisões arquiteturais deverão ser registradas em `docs/decisions/`.

## 12. Critérios de sucesso

O primeiro incremento funcional será considerado concluído quando:

- Os cálculos genéricos de juros compostos estiverem documentados e testados.
- O sistema aceitar dois cenários com capital inicial e prazo equivalentes.
- Os montantes e rendimentos brutos estimados forem calculados corretamente.
- A diferença entre os resultados for apresentada.
- As entradas inválidas forem rejeitadas.
- As limitações do modelo forem informadas.
- A aplicação puder ser executada localmente conforme as instruções do projeto.

O MVP ampliado será considerado funcional quando, adicionalmente:

- Os produtos financeiros suportados forem representados adequadamente.
- As comparações utilizarem regras compatíveis com cada produto.
- Os dados históricos utilizados forem rastreáveis.
- Os cálculos líquidos implementados considerarem as regras e os custos aplicáveis.
- As análises puderem ser reproduzidas a partir dos dados e premissas registrados.
- A documentação refletir o comportamento efetivamente implementado.

Não será considerado critério de sucesso alcançar determinada rentabilidade de mercado.

## 13. Riscos e mitigações

| Risco | Mitigação |
|---|---|
| Cálculos incorretos | Fórmulas documentadas e testes automatizados |
| Comparações incompatíveis | Premissas equivalentes e convenções explícitas |
| Dados desatualizados | Registro de fontes e datas de referência |
| Simplificações interpretadas como recomendações | Limitações visíveis e ausência de ranking universal |
| Crescimento excessivo do escopo | Desenvolvimento incremental |
| Falsa sensação de garantia | Separação entre projeções e resultados observados |
| Exposição de dados pessoais | Execução local e transmissão externa mínima |

## 14. Decisões ainda pendentes

- Quais fontes oficiais serão adotadas para cada indicador.
- Quais convenções de taxas e calendários serão necessárias para cada produto.
- Como tratar tributação e custos por categoria.
- Quais regras serão usadas para calcular retornos líquidos e reais.
- Como representar a incerteza de taxas futuras.
- Quais campos serão obrigatórios no cadastro de cada produto.
- Como medir concentração e diversificação.
- Como avaliar adequação aos objetivos financeiros.
- Quais informações serão armazenadas para reproduzir análises históricas.
- Como tratar produtos com informações insuficientes.

Essas decisões deverão ser resolvidas antes da implementação das funcionalidades correspondentes.

## 15. Documentação relacionada

- `README.md` — apresentação e instruções de execução.
- `docs/README.md` — índice da documentação.
- `docs/architecture.md` — arquitetura do sistema.
- `docs/domain-model.md` — conceitos e entidades.
- `docs/financial-rules.md` — fórmulas e convenções financeiras.
- `docs/roadmap.md` — etapas de desenvolvimento.
- `docs/decisions/001-modular-monolith.md` — decisão pelo monólito modular.

## 16. Limitações e aviso

O Aporte é um projeto educacional open-source em desenvolvimento. Os resultados dependem da qualidade dos dados, das regras implementadas e das premissas fornecidas.

As análises não garantem rentabilidade e não substituem a verificação independente das informações ou aconselhamento financeiro profissional.
