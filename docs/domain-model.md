# Modelo de Domínio

## 1. Objetivo

Este documento descreve os principais conceitos do domínio financeiro do Aporte, suas responsabilidades e as regras que orientam os cálculos e as comparações.

O Aporte começa como uma aplicação local de comparação de cenários hipotéticos de investimento. A implementação inicial utiliza juros compostos com taxa efetiva anual constante.

Os cálculos de produtos financeiros reais serão adicionados posteriormente, com regras específicas para cada produto.

## 2. Conceitos do domínio

### 2.1. InvestmentScenario

Representa um cenário hipotético de investimento.

**Atributos:**

- `initial_amount`: capital inicial, representado por `Decimal`.
- `annual_rate`: taxa efetiva anual em formato decimal, representada por `Decimal`.
- `years`: prazo inteiro positivo, expresso em anos.

**Invariantes:**

- O capital inicial deve ser maior que zero.
- A taxa anual não pode ser negativa.
- O prazo deve ser um número inteiro positivo.
- Os valores monetários e as taxas utilizadas no domínio devem respeitar seus tipos esperados.

O objeto é imutável após sua criação, utilizando `dataclass(frozen=True)`.

**Responsabilidade:** representar os dados e garantir as condições básicas de validade de um cenário.

Arquivo: `app/domain/investment.py`

### 2.2. CompoundInterestCalculator

Responsável pelo cálculo do montante de um cenário usando juros compostos.

**Fórmula:**

M = C × (1 + i)^n

Onde:

- `M`: montante final.
- `C`: capital inicial.
- `i`: taxa efetiva anual expressa em formato decimal.
- `n`: número de anos.

O cálculo pressupõe que a taxa efetiva anual permanece constante durante todo o prazo.

O resultado é retornado como `Decimal`, sem arredondamento monetário intermediário.

**Responsabilidade:** executar o cálculo matemático, sem depender da API, de bancos de dados ou de fontes externas.

Arquivo: `app/domain/services/compound_interest.py`

### 2.3. InvestmentAnalysisService

Coordena a comparação de dois cenários hipotéticos.

**Responsabilidades:**

- Receber dois cenários.
- Validar se ambos possuem o mesmo capital inicial e o mesmo prazo.
- Calcular os montantes finais.
- Arredondar os montantes para duas casas decimais, usando `ROUND_HALF_UP`.
- Calcular os rendimentos brutos e a diferença absoluta entre os montantes arredondados.
- Identificar qual cenário apresenta o maior montante, ou se ambos são iguais.
- Informar as limitações da análise.

A identificação do maior montante é apenas uma comparação matemática. Não representa uma recomendação individual de investimento.

Arquivo: `app/services/analysis.py`

## 3. Schemas e API

### 3.1. InvestmentScenarioRequest

Define o formato dos dados de entrada de um cenário na API.

É responsável pela validação estrutural das entradas, incluindo limites de valores, taxa e prazo.

Arquivo: `app/schemas/investment.py`

### 3.2. InvestmentComparisonRequest

Recebe os cenários A e B que serão comparados.

Os requisitos de igualdade entre capital inicial e prazo são verificados pelo serviço de análise.

### 3.3. InvestmentComparisonResponse

Define a resposta da comparação, incluindo:

- Capital inicial.
- Prazo.
- Taxa anual de cada cenário.
- Montante final bruto de cada cenário.
- Rendimento bruto de cada cenário.
- Diferença absoluta.
- Identificação do cenário com maior montante.
- Limitações da análise.

### 3.4. API

O endpoint `POST /api/v1/investments/compare` recebe a solicitação, converte os dados em objetos de domínio, executa a análise e devolve a resposta.

Arquivo: `app/api/routes.py`

## 4. Regras financeiras atuais

1. O cálculo utiliza juros compostos.
2. A taxa é efetiva anual, não nominal nem mensal.
3. A taxa é considerada constante durante todo o prazo.
4. O prazo é expresso em anos inteiros positivos.
5. O capital inicial deve ser idêntico nos dois cenários.
6. O prazo deve ser idêntico nos dois cenários.
7. O montante final é arredondado para duas casas decimais antes do cálculo do rendimento e da diferença.
8. O rendimento bruto corresponde ao montante final arredondado menos o capital inicial.
9. A diferença absoluta corresponde à diferença entre os montantes finais arredondados.
10. A análise não considera impostos, custos, inflação, risco, liquidez ou alterações futuras nas taxas.

Os limites específicos de entrada da API também são definidos no schema. Esses limites técnicos não devem ser confundidos com regras universais do mercado financeiro.

## 5. Limites do modelo atual

O modelo ainda não representa integralmente investimentos reais.

Não contempla:

- Indexadores financeiros, como CDI ou Selic.
- Taxas variáveis ao longo do tempo.
- Capitalização com convenções específicas de cada produto.
- Imposto de renda ou IOF.
- Taxas de custódia, tarifas ou outros custos.README
- Datas de aplicação, vencimento ou resgate.
- Dias úteis, calendários financeiros ou contagem de dias.
- Retorno real após a inflação.
- Risco de crédito, liquidez ou oscilação de preços.

Por isso, os resultados atuais devem ser interpretados como estimativas matemáticas brutas, e não como projeções garantidas de rentabilidade.

## 6. Evolução prevista

O domínio poderá ser ampliado gradualmente para incluir:

1. Regras específicas para CDB pós-fixado e Tesouro Selic.
2. Modelagem explícita de indexadores e fontes de dados.
3. Cálculo de impostos e custos.
4. Comparação de retornos líquidos e reais.
5. Representação de prazos, vencimentos e liquidez.
6. Modelagem de carteira e objetivos financeiros.

Cada extensão deverá introduzir apenas os conceitos necessários para representar corretamente a nova regra de negócio, com testes automatizados e documentação correspondente.

## 7. Princípio arquitetural

O domínio financeiro deve permanecer independente de detalhes de infraestrutura.

As regras de cálculo não devem depender de FastAPI, de bancos de dados ou de integrações externas. A API recebe e devolve dados; os serviços coordenam as operações; o domínio representa os conceitos e executa as regras financeiras.

Essa separação facilita testar o comportamento financeiro isoladamente e evoluir a aplicação sem acoplar seus cálculos à infraestrutura.
