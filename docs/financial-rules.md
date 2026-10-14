# Regras Financeiras

## 1. Objetivo

Documentar as convenções, fórmulas e comportamentos numéricos utilizados pelo motor financeiro do Aporte.

O Aporte começa como uma aplicação local de comparação de cenários hipotéticos de investimento. A implementação inicial utiliza juros compostos com taxa efetiva anual constante.

As regras devem ser implementadas de forma testável e acompanhadas de exemplos com resultados conhecidos.

## 2. Convenções numéricas, de taxa e prazo

- **Moeda e valores monetários:** A moeda inicial é o real brasileiro (BRL). Valores monetários devem utilizar representação decimal exata (`Decimal`) para evitar imprecisões de ponto flutuante. O capital inicial (`initial_amount` ou `C`) deve ser estritamente maior que zero (`C > 0`).
- **Taxa efetiva anual:** A taxa de juros (`annual_rate` ou `i`) é expressa como taxa efetiva anual, e não taxa nominal nem mensal. Deve ser representada por `Decimal` em formato decimal antes do cálculo (por exemplo, 10% ao ano corresponde a `0.10`). A taxa não pode ser negativa (`i >= 0`) e é considerada constante ao longo de todo o prazo.
- **Prazo:** O prazo (`years` ou `n`) é expresso como um número inteiro positivo de anos (`int`, `n > 0`). O modelo atual não contempla frações de ano, datas de aplicação/resgate, contagem de dias úteis ou corridos, nem calendários financeiros.
- **Arredondamento:**
  - O cálculo matemático do montante é executado sem arredondamento monetário intermediário, preservando a precisão integral do tipo `Decimal`.
  - Os montantes finais são arredondados para duas casas decimais utilizando a convenção `ROUND_HALF_UP` (meio para cima).
  - O rendimento bruto e a diferença absoluta entre cenários são calculados a partir dos montantes finais já arredondados.

## 3. Juros compostos

O cálculo do montante de um cenário hipotético de investimento utiliza juros compostos com taxa efetiva anual constante.

**Fórmula:**

M = C × (1 + i)^n

Onde:

- `M`: montante final.
- `C`: capital inicial.
- `i`: taxa efetiva anual expressa em formato decimal.
- `n`: número de anos.

**Premissas e comportamento:**

- A taxa efetiva anual permanece constante durante todo o prazo.
- O resultado é retornado como `Decimal`, sem arredondamento monetário intermediário.
- Esta fórmula não contempla impostos, custos, aportes adicionais, oscilação de taxa, inflação, risco ou liquidez.

## 4. Arredondamento e comparação de cenários

Ao analisar e comparar dois cenários hipotéticos de investimento:

1. **Requisitos de comparabilidade:** Ambos os cenários devem possuir obrigatoriamente o mesmo capital inicial e o mesmo prazo em anos.
2. **Arredondamento do montante final:** Cada montante final calculado é arredondado para duas casas decimais utilizando o critério `ROUND_HALF_UP` (meio para cima).
3. **Rendimento bruto:** Corresponde ao montante final arredondado menos o capital inicial:
   `rendimento_bruto = montante_final_arredondado - capital_inicial`
4. **Diferença absoluta:** Corresponde à diferença absoluta entre os montantes finais arredondados dos dois cenários comparados:
   `diferenca_absoluta = |montante_a_arredondado - montante_b_arredondado|`
5. **Classificação:** Identifica qual cenário apresenta o maior montante final arredondado, ou se ambos são equivalentes (`equal`). Essa identificação é estritamente matemática e não constitui recomendação individual de investimento.

### Exemplos numéricos de referência

**Exemplo 1 (sem resíduo de centavos):**

- Capital inicial: R$ 1.000,00
- Taxa efetiva anual: 10% ao ano (`0.10`)
- Prazo: 3 anos
- Cálculo exato (sem arredondamento intermediário): `1000 × (1 + 0.10)^3 = 1331.000000`
- Montante final arredondado (`ROUND_HALF_UP`): R$ 1.331,00
- Rendimento bruto: R$ 331,00 (`1331.00 - 1000.00`)

**Exemplo 2 (com arredondamento ROUND_HALF_UP):**

- Capital inicial: R$ 1.000,00
- Taxa efetiva anual: 12% ao ano (`0.12`)
- Prazo: 3 anos
- Cálculo exato (sem arredondamento intermediário): `1000 × (1 + 0.12)^3 = 1404.928`
- Montante final arredondado (`ROUND_HALF_UP`): R$ 1.404,93 (o dígito 8 na terceira casa decimal arredonda 92 para 93 centavos)
- Rendimento bruto: R$ 404,93 (`1404.93 - 1000.00`)

**Comparação entre Exemplo 1 e Exemplo 2:**

- Capital inicial compartilhado: R$ 1.000,00
- Prazo compartilhado: 3 anos
- Diferença absoluta: `|1404.93 - 1331.00| = R$ 73,93`
- Cenário com maior montante: Exemplo 2

## 5. Rentabilidade nominal e real

Quando a rentabilidade nominal e a inflação se referem ao mesmo período:

r_real = (1 + r_nominal) / (1 + inflação) - 1

A rentabilidade real representa a variação do poder de compra.

As taxas devem ser expressas como retornos decimais. Não se deve combinar períodos diferentes sem uma conversão apropriada.

No modelo atual, a inflação não é considerada nas análises, tratando-se apenas de estimativas nominais brutas.

## 6. Retorno bruto e líquido

No modelo atual, o rendimento bruto corresponde ao montante final arredondado menos o capital inicial, sem desconto de impostos ou custos operacionais.

O retorno líquido deve considerar os tributos (como Imposto de Renda e IOF) e custos (como taxas de custódia e tarifas) efetivamente aplicáveis ao produto, ao prazo e às condições do investimento.

Não implementar uma fórmula tributária genérica para todos os produtos. As regras de tributação deverão ser especificadas por modalidade e período de vigência quando essa funcionalidade for implementada.

## 7. Taxas e indexadores

Uma taxa precisa ser identificada pelo menos por:
- valor;
- unidade temporal;
- convenção;
- período de referência.

Indicadores como Selic, CDI/Taxa DI e IPCA possuem funções e metodologias distintas.

O modelo atual contempla exclusivamente taxas efetivas anuais prefixadas hipotéticas. Um produto vinculado a um indexador exige a aplicação das condições contratuais correspondentes e fontes de dados de mercado, não se devendo substituir automaticamente um indicador por outro.

## 8. Projeções e limitações

Toda projeção deve explicitar suas hipóteses, como:
- taxa constante ou cenário de taxas;
- prazo;
- periodicidade de capitalização;
- tributação considerada;
- inflação considerada;
- aportes adicionais.

Uma projeção é um cenário matemático calculado, não uma promessa ou garantia de rentabilidade.

A análise não considera impostos, custos, inflação, risco de crédito, liquidez ou alterações futuras nas taxas de juros.

## 9. Testes obrigatórios

Cada regra implementada deverá possuir:
- casos de referência com resultados conhecidos;
- testes de limites e entradas inválidas (capital menor ou igual a zero, taxa negativa, prazo menor ou igual a zero ou não inteiro, cenários com capitais ou prazos divergentes na comparação);
- testes de arredondamento, garantindo a ausência de arredondamento monetário intermediário e a correta aplicação de `ROUND_HALF_UP` para duas casas decimais no montante final;
- testes para períodos e taxas diferentes;
- justificativa da fórmula e de suas hipóteses.

## 10. Itens ainda não especificados

- Conversão entre taxas anuais, mensais e diárias.
- Convenções de dias úteis e corridos.
- Cálculo de produtos pós-fixados e indexadores (CDI, Selic, IPCA).
- Tributação de cada modalidade (tabela regressiva de IR, regras de IOF, isenções).
- Custos, taxas administrativas e taxas de custódia.
- Tratamento de resgates e aportes periódicos.
- Metodologia de retorno real de uma carteira com fluxos de caixa.

Nenhuma dessas regras deverá ser considerada implementada apenas por estar documentada aqui.
